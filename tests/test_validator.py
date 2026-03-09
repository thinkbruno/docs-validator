from cnpj_validator import validate


def test_valid_cnpj():
    assert validate("11222333000181") is True


def test_invalid_cnpj():
    assert validate("11222333000182") is False


def test_formatted_cnpj():
    assert validate("11.222.333/0001-81") is True
