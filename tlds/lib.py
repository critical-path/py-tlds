"""Library used by py-tlds."""


from collections import OrderedDict

from hashlib import md5

from re import (
    compile,
    match,
    search
)

from requests import get

from tlds.err import ValidationError


class TopLevelDomainGetter(object):
    """Retrieves and validates a list of top-level domains (TLDs)
       from the Internet Assigned Names Authority (IANA).

       Returns
       -------
       self.results : ordered dict
           Contains version number, last update, and valid TLDs."""

    def __init__(self):
        """Instantiates TopLevelDomainGetter."""

        self._urls = {
            "tld": "http://data.iana.org/TLD/tlds-alpha-by-domain.txt",
            "md5": "http://data.iana.org/TLD/tlds-alpha-by-domain.txt.md5"
        }

        self._data = {
            "tld": None,
            "md5": None
        }

        self._digests = {
            "actual": None,
            "expected": None
        }

        self._is_valid = False

        self._patterns = {
            "other": compile("Version [A-Za-z0-9,: ]{1,}"),
            "tld": compile("[A-Z0-9-]")
        }

        self.results = OrderedDict({
            "version": None,
            "updated": None,
            "tlds": []
        })

    def _get_tld_data(self):
        """Sends HTTP GET request to IANA.  Retrieves TLD data."""

        response = get(self._urls["tld"])
        response.raise_for_status()

        response_body = response.text
        self._data["tld"] = response_body

    def _get_md5_data(self):
        """Sends HTTP GET request to IANA.  Retrieves MD5 data."""

        response = get(self._urls["md5"])
        response.raise_for_status()

        response_body = response.text
        self._data["md5"] = response_body

    def _get_actual_digest(self):
        """Computes MD5 digest from retrieved TLD data."""

        data = bytes(self._data["tld"], "utf-8")
        digest = md5(data).hexdigest()
        self._digests["actual"] = digest

    def _get_expected_digest(self):
        """Extracts MD5 digest from retrieved MD5 data."""

        data = self._data["md5"].split()
        digest = data[0]
        self._digests["expected"] = digest

    def _compare_digests(self):
        """Compares MD5 digests."""

        if self._digests["actual"] == self._digests["expected"]:
            self._is_valid = True

    def _get_tlds(self):
        """Parses TLD data, looking for version number, 
           last update, and valid TLDs."""

        data = self._data["tld"].split("\n")

        for datum in data:
            if search(self._patterns["other"], datum):
                other = search(self._patterns["other"], datum).group().split(",")
                version, updated = other

                self.results["version"] = version.strip()
                self.results["updated"] = updated.strip()

            if match(self._patterns["tld"], datum):
                self.results["tlds"].append(datum)

    def get(self):
        """Calls private methods to get, validate, and parse data.
           Raises ValidationError if MD5 digests differ.

           Returns
           -------
           self.results : ordered dict
               Contains version number, last update, and valid TLDs."""

        self._get_tld_data()
        self._get_md5_data()

        self._get_actual_digest()
        self._get_expected_digest()
        self._compare_digests()

        if self._is_valid:
            self._get_tlds()
            return self.results

        else:
            raise ValidationError("Our MD5 digest ({}) did not match that provided by IANA ({}).  Please try again.".format(self._digests["actual"], self._digests["expected"]))
