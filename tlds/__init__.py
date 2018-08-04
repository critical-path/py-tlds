"""util that retrieves and validates a list of top-level domains from the internet assigned names authority."""


from tlds.lib import TopLevelDomainGetter

from tlds.utils import write_results


__version__ = "1.0.0"

__author__ = "critical-path"

__all__ = [
    "TopLevelDomainGetter",
    "write_results"
]
