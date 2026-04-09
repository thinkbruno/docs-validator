from docs_validator.validator import validate


def test_validate_cnpj():
    result = validate("11222333000181")

    assert result["type"] == "CNPJ"
    assert result["country"] == "BR"
    assert isinstance(result["valid"], bool)


def test_validate_cnpj_with_mask():
    result = validate("11.222.333/0001-81")

    assert result["type"] == "CNPJ"


def test_validate_alphanumeric_cnpj():
    result = validate("AB12CD34EF5601")

    assert result["type"] == "CNPJ"
    assert result["country"] == "BR"


def test_validate_cpf():
    result = validate("12345678909")

    assert result["type"] == "CPF"
    assert result["country"] == "BR"


def test_validate_invalid():
    result = validate("ABC")

    assert result["type"] is None
    assert result["valid"] is False


def test_validate_empty():
    result = validate("")

    assert result["type"] is None
    assert result["valid"] is False


def test_validate_with_special_chars():
    result = validate("!!!")

    assert result["valid"] is False
