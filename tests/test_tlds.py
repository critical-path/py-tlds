from os import (
    remove,
    stat
)

from tlds.cli import get_tlds

from tlds.err import ValidationError

from tlds.lib import TopLevelDomainGetter

from tlds.utils import write_results

from click.testing import CliRunner

from pytest import raises

from responses import (
    activate,
    add,
    GET
)

from constants import (
    DATA_MD5_INVALID,
    DATA_MD5_VALID,
    DATA_TLD,
    TLDS,
    TLDS_FILENAME,
    TLDS_JSON,
    URL_MD5,
    URL_TLD
)


@activate
def test_lib_with_invalid_tlds():
    add(
        method=GET,
        url=URL_TLD,
        body=DATA_TLD,
        status=200
    )

    add(
        method=GET,
        url=URL_MD5,
        body=DATA_MD5_INVALID,
        status=200
    )

    with raises(ValidationError) as exception:
        tld_getter = TopLevelDomainGetter()
        tlds = tld_getter.get()

    assert "Our MD5 digest ({}) did not match that provided by IANA ({}).  Please try again.".format(tld_getter._digests["actual"], tld_getter._digests["expected"]) in str(exception.value)


@activate
def test_lib_with_valid_tlds():
    add(
        method=GET,
        url=URL_TLD,
        body=DATA_TLD,
        status=200
    )

    add(
        method=GET,
        url=URL_MD5,
        body=DATA_MD5_VALID,
        status=200
    )

    tld_getter = TopLevelDomainGetter()
    tlds = tld_getter.get()

    assert tlds == TLDS


@activate
def test_lib_and_utils_with_valid_tlds_and_write_results():
    add(
        method=GET,
        url=URL_TLD,
        body=DATA_TLD,
        status=200
    )

    add(
        method=GET,
        url=URL_MD5,
        body=DATA_MD5_VALID,
        status=200
    )

    tld_getter = TopLevelDomainGetter()
    tlds = tld_getter.get()
    write_results(tlds)

    assert tlds == TLDS
    assert stat(TLDS_FILENAME)
    remove(TLDS_FILENAME)


@activate
def test_cli_with_no_write():
    add(
        method=GET,
        url=URL_TLD,
        body=DATA_TLD,
        status=200
    )

    add(
        method=GET,
        url=URL_MD5,
        body=DATA_MD5_VALID,
        status=200
    )

    runner = CliRunner()

    result = runner.invoke(
        get_tlds
    )

    assert result.exit_code == 0
    assert result.output == TLDS_JSON


@activate
def test_cli_with_write_long():
    add(
        method=GET,
        url=URL_TLD,
        body=DATA_TLD,
        status=200
    )

    add(
        method=GET,
        url=URL_MD5,
        body=DATA_MD5_VALID,
        status=200
    )

    runner = CliRunner()

    result = runner.invoke(
        get_tlds,
        [
            "--write"
        ]
    )

    assert result.exit_code == 0
    assert result.output == TLDS_JSON
    assert stat(TLDS_FILENAME)
    remove(TLDS_FILENAME)


@activate
def test_cli_with_write_short():
    add(
        method=GET,
        url=URL_TLD,
        body=DATA_TLD,
        status=200
    )

    add(
        method=GET,
        url=URL_MD5,
        body=DATA_MD5_VALID,
        status=200
    )

    runner = CliRunner()

    result = runner.invoke(
        get_tlds,
        [
            "-w"
        ]
    )

    assert result.exit_code == 0
    assert result.output == TLDS_JSON
    assert stat(TLDS_FILENAME)
    remove(TLDS_FILENAME)
