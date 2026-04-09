from docs_validator.detect import detect


def test_detect_valid_cpf():
    result = detect("12345678909")

    assert result["type"] == "CPF"
    assert result["country"] == "BR"
    assert isinstance(result["valid"], bool)


def test_detect_cpf_with_mask():
    result = detect("123.456.789-09")

    assert result["type"] == "CPF"


def test_detect_valid_cnpj():
    result = detect("11222333000181")

    assert result["type"] == "CNPJ"
    assert result["country"] == "BR"


def test_detect_cnpj_with_mask():
    result = detect("11.222.333/0001-81")

    assert result["type"] == "CNPJ"


def test_detect_alphanumeric_cnpj():
    result = detect("AB12CD34EF5601")

    assert result["type"] == "CNPJ"
    assert result["country"] == "BR"


def test_detect_invalid_document():
    result = detect("ABC")

    assert result["type"] is None
    assert result["country"] is None
    assert result["valid"] is False


def test_detect_empty():
    result = detect("")

    assert result["type"] is None
    assert result["valid"] is False
