from collections import OrderedDict

from hashlib import md5

from re import (
    compile,
    match,
    search
)

from requests import get

from tlds.tlds_err import ValidationError


class TopLevelDomainGetter(object):
    """Retrieves and validates a list of top-level domains (TLDs)
    from the Internet Assigned Names Authority (IANA).


    Returns
    -------
    self.results : ordered dict
        Contains version number, last update, and valid TLDs
    """

    def __init__(self):
        """Instantiates TopLevelDomainGetter."""

        self.__urls__ = {
            "tld": "http://data.iana.org/TLD/tlds-alpha-by-domain.txt",
            "md5": "http://data.iana.org/TLD/tlds-alpha-by-domain.txt.md5"
        }

        self.__data__ = {
            "tld": None,
            "md5": None
        }

        self.__digests__ = {
            "actual": None,
            "expected": None
        }

        self.__is_valid__ = False

        self.__patterns__ = {
            "other": compile("Version [A-Za-z0-9,: ]{1,}"),
            "tld": compile("[A-Z0-9-]")
        }

        self.results = OrderedDict({
            "version": None,
            "updated": None,
            "tlds": []
        })

    def __get_tld_data__(self):
        """Sends HTTP GET request to IANA.
        Retrieves TLD data."""

        response = get(self.__urls__["tld"])
        response.raise_for_status()

        response_body = response.text
        self.__data__["tld"] = response_body

    def __get_md5_data__(self):
        """Sends HTTP GET request to IANA.
        Retrieves MD5 data."""

        response = get(self.__urls__["md5"])
        response.raise_for_status()

        response_body = response.text
        self.__data__["md5"] = response_body

    def __get_actual_digest__(self):
        """Computes MD5 digest from retrieved TLD data."""

        data = bytes(self.__data__["tld"], "utf-8")
        digest = md5(data).hexdigest()
        self.__digests__["actual"] = digest

    def __get_expected_digest__(self):
        """Extracts MD5 digest from retrieved MD5 data."""

        data = self.__data__["md5"].split()
        digest = data[0]
        self.__digests__["expected"] = digest

    def __compare_digests__(self):
        """Compares MD5 digests."""

        if self.__digests__["actual"] == self.__digests__["expected"]:
            self.__is_valid__ = True

    def __get_tlds__(self):
        """Parses TLD data, looking for version number,
       last update, and valid TLDs."""

        data = self.__data__["tld"].split("\n")

        for datum in data:
            if search(self.__patterns__["other"], datum):
                other = search(self.__patterns__["other"], datum).group()
                other = other.split(",")
                version = other[0].strip()
                updated = other[1].strip()

                self.results["version"] = version
                self.results["updated"] = updated

            elif match(self.__patterns__["tld"], datum):
                self.results["tlds"].append(datum)

    def get(self):
        """Calls private methods to get, validate, and parse data.
        Raises ValidationError if MD5 digests differ.


        Returns
        -------
        self.results : ordered dict
            Contains version number, last update, and valid TLDs
        """

        self.__get_tld_data__()
        self.__get_md5_data__()

        self.__get_actual_digest__()
        self.__get_expected_digest__()
        self.__compare_digests__()

        if self.__is_valid__:
            self.__get_tlds__()
            return self.results

        else:
            raise ValidationError("Our MD5 digest ({}) did not match that provided by IANA ({}).  Please try again.".format(self.__digests__["actual"], self.__digests__["expected"]))
