[![Build Status](https://travis-ci.com/critical-path/py-tlds.svg?branch=master)](https://travis-ci.com/critical-path/py-tlds) [![Coverage Status](https://coveralls.io/repos/github/critical-path/py-tlds/badge.svg)](https://coveralls.io/github/critical-path/py-tlds)

## py-tlds v1.0.0

py-tlds is a util that retrieves and validates a list of top-level domains (TLDs) from the Internet Assigned Names Authority.


## Dependencies

py-tlds requires Python 3.x and the pip package.  It also requires the following packages for usage and testing.

__Usage__:
- click
- requests

__Testing__:
- coveralls
- pytest
- pytest-cov
- radon
- responses


## Installing py-tlds with test cases and testing dependencies

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command and the `--editable` option.

```
sudo pip install --editable .[test]
```


## Installing py-tlds without test cases or testing dependencies

1. Clone or download this repository.

2. Using `sudo`, run `pip` with the `install` command.

```
sudo pip install .
```


## Using py-tlds from the command line

To retrieve and validate a list of TLDs, simply run `tlds`.

```
tlds
```

To write the results to disk, run `tlds` with either the `--write` or the `-w` option.

```
tlds --write
tld -w
```


## Using py-tlds from within Python

1. Import `TopLevelDomainGetter` and `write_results`.
2. Instantiate `TopLevelDomainGetter` and call its `get` method.
3. Call the `write_results` function.


```
from tlds import (
  TopLevelDomainGetter,
  write_results
)

tld_getter = TopLevelDomainGetter()
tlds = tld_getter.get()
write_results(tlds)
```


## Testing py-tlds after installation

1. Run `radon` with the `mi` command and the `--show` option.

```
radon mi --show tlds
```

2. Run `pytest` with with `-vv`, `--cov`, and `cov-report` options.

```
pytest -vv --cov --cov-report=term-missing
```
