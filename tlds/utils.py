"""Utility function used by py-tlds."""


from json import dumps


def write_results(tlds=None):
    """Writes results to disk.

    Parameters
    ----------
    tlds : ordered dict or str
        Contains version number, last update, and valid TLDs

    Returns
    -------
    N/A
    """

    filename = "iana-tlds.json"

    if isinstance(tlds, dict):
        tlds = dumps(tlds, indent=2)

    with open(filename, "w") as output:
        output.write(tlds)
