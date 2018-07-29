## py-tlds v1.0.0

py-tlds is a util that retrieves and validates a list of top-level domains (TLDs) from the Internet Assigned Names Authority.


## Dependencies

py-tlds requires Python as well as the pip, click, requests, pylint, pytest, pytest-cov, and responses packages.


## Installing py-tlds with test cases and testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip3 with the install command and the --editable option.

```
sudo pip3 install --editable .[test] .
```

## Installing py-tlds without test cases or testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip3 with the install command.

```
sudo pip3 install .
```

## Using py-tlds from the command line

To retrieve and validate a list of TLDs, simply run tlds.

```
tlds
```

To write the results to disk, run tlds with either the --write or the -w option.

```
tlds --write
tld -w
```

## Using py-tlds from within Python

1. Import TopLevelDomainGetter and write_results.
2. Instantiate TopLevelDomainGetter and call its get method.
3. Call the write_results function.


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

1. Run pylint.

```
pylint tlds 
```

2. Change to the tests directory.

```
cd ./tests
```

3. Run pytest with with -vv, --cov, and cov-report options.

```
pytest -vv --cov=tlds --cov-report=term-missing
```
