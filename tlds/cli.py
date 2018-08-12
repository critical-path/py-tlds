"""Command-line interface for py-tlds."""


from json import dumps

from click import (
    command,
    echo,
    option
)

from tlds.lib import TopLevelDomainGetter

from tlds.utils import write_results


@command()
@option("--write", "-w", is_flag=True, help="Write results to disk")
def get_tlds(write=False):
    """Util that retrieves and validates a list of top-level domains
    from the Internet Assigned Names Authority."""

    tld_getter = TopLevelDomainGetter()
    tlds = tld_getter.get()
    tlds = dumps(tlds, indent=2)

    if write:
        write_results(tlds=tlds)

    echo(tlds)


if __name__ == "__main__":
    get_tlds()
