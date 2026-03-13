from docs_validator.br.cnpj import validate_cnpj


def test_valid_cnpj():
    assert validate_cnpj("11222333000181")


def test_valid_formatted_cnpj():
    assert validate_cnpj("11.222.333/0001-81")


def test_invalid_cnpj():
    assert not validate_cnpj("11222333000182")
