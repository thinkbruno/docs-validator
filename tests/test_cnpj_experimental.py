import pytest

from docs_validator.experimental.cnpj_alphanumeric import (
    validate_cnpj_alphanumeric,
    CHAR_MAP,
)


def test_invalid_length():
    assert validate_cnpj_alphanumeric("ABC123") is False


def test_invalid_characters():
    assert validate_cnpj_alphanumeric("AB12CD34EF56@1") is False


def test_invalid_last_digits_not_numeric():
    assert validate_cnpj_alphanumeric("AB12CD34EF56AA") is False


def test_algorithm_runs():
    doc = "12ABC34501DE35"

    result = validate_cnpj_alphanumeric(doc)

    assert isinstance(result, bool)


def test_invalid_dv():
    # força DV inválido
    assert validate_cnpj_alphanumeric("AB12CD34EF5600") is False


def test_char_map_numeric():
    assert CHAR_MAP["0"] == 0
    assert CHAR_MAP["9"] == 9


def test_char_map_alpha():
    assert CHAR_MAP["A"] == 10
    assert CHAR_MAP["Z"] == 35


def test_char_map_invalid():
    with pytest.raises(KeyError):
        _ = CHAR_MAP["@"]


def test_lowercase_input():
    result = validate_cnpj_alphanumeric("ab12cd34ef5601")

    assert isinstance(result, bool)


def test_input_with_mask():
    result = validate_cnpj_alphanumeric("AB12.CD34/EF56-01")

    assert isinstance(result, bool)
