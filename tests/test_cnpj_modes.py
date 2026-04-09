from docs_validator.br.cnpj import validate_cnpj


def test_strict_mode_valid_numeric():
    assert validate_cnpj("11222333000181", mode="strict") is True


def test_strict_mode_invalid_dv():
    assert validate_cnpj("11222333000182", mode="strict") is False


def test_strict_mode_alphanumeric_only_structure():
    # mesmo sem saber DV, deve aceitar estrutura
    assert validate_cnpj("AB12CD34EF5601", mode="strict") is True


def test_loose_mode_valid_format_numeric():
    assert validate_cnpj("12345678000100", mode="loose") is True


def test_loose_mode_valid_format_alphanumeric():
    assert validate_cnpj("AB12CD34EF5601", mode="loose") is True


def test_loose_mode_invalid_format():
    assert validate_cnpj("ABC", mode="loose") is False


def test_experimental_mode_numeric():
    assert validate_cnpj("11222333000181", mode="experimental") is True


def test_experimental_mode_alphanumeric_runs():
    result = validate_cnpj("AB12CD34EF5601", mode="experimental")

    assert isinstance(result, bool)


def test_experimental_mode_invalid_format():
    assert validate_cnpj("ABC", mode="experimental") is False


def test_loose_mode_ignores_validate_dv():
    assert validate_cnpj("12345678000100", mode="loose", validate_dv=True) is True


def test_strict_mode_respects_validate_dv():
    assert validate_cnpj("12345678000100", mode="strict", validate_dv=False) is True
