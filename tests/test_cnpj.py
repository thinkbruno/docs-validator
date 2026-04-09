import pytest

from docs_validator.br.cnpj import validate_cnpj


def test_valid_cnpj():
    assert validate_cnpj("11222333000181") is True


def test_valid_cnpj_with_mask():
    assert validate_cnpj("11.222.333/0001-81") is True


def test_invalid_cnpj_wrong_dv():
    assert validate_cnpj("11222333000182") is False


def test_invalid_cnpj_repeated_digits():
    assert validate_cnpj("11111111111111") is False


def test_invalid_cnpj_short():
    assert validate_cnpj("123") is False


def test_alphanumeric_valid_structure():
    assert validate_cnpj("AB12CD34EF5601") is True


def test_alphanumeric_invalid_structure():
    assert validate_cnpj("AB12CD34EF56AA") is False


def test_validate_dv_false():
    assert validate_cnpj("12345678000100", validate_dv=False) is True


def test_empty_input():
    assert validate_cnpj("") is False


def test_none_input():
    with pytest.raises(AttributeError):
        validate_cnpj(None)
