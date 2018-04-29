from json import dumps


def write_results(tlds=None):
    """Write results to disk.

    Parameters
    ----------
    tlds : ordered dict or str
        Contains version number, last update, and valid TLDs
    """

    filename = "iana-tlds.json"

    if isinstance(tlds, dict):
        tlds = dumps(tlds, indent=2)

    with open(filename, "w") as output:
        output.write(tlds)
