from collections import OrderedDict

from hashlib import md5

from json import dumps


URL_TLD = "http://data.iana.org/TLD/tlds-alpha-by-domain.txt"

URL_MD5 = "http://data.iana.org/TLD/tlds-alpha-by-domain.txt.md5"

DATA_TLD = """# Version 2018042900, Last Updated Sun Apr 29 00:00:00 2018 UTC
AB
CD
EF
GH
IJ
KL
MN
OP
QR
ST
UV
WX
YZ"""

MD5_VALID = md5(bytes(DATA_TLD, "utf-8")).hexdigest()

DATA_MD5_VALID = "{}  tlds-alpha-by-domain.txt".format(MD5_VALID)

DATA_MD5_INVALID = "invalid-md5  tlds-alpha-by-domain.txt"

TLDS = OrderedDict({
  "version": "Version 2018042900",
  "updated": "Last Updated Sun Apr 29 00:00:00 2018 UTC",
  "tlds": [
      "AB",
      "CD",
      "EF",
      "GH",
      "IJ",
      "KL",
      "MN",
      "OP",
      "QR",
      "ST",
      "UV",
      "WX",
      "YZ"
  ]
})

TLDS_JSON = dumps(TLDS, indent=2) + "\n"

TLDS_FILENAME = "iana-tlds.json"
