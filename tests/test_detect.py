from docs_validator import detect


def test_detect_cpf():

    result = detect("52998224725")

    assert result["type"] == "CPF"
    assert result["country"] == "BR"
    assert result["valid"] is True


def test_detect_cnpj():

    result = detect("11222333000181")

    assert result["type"] == "CNPJ"
    assert result["country"] == "BR"
    assert result["valid"] is True


def test_invalid_doc():

    result = detect("123")

    assert result["valid"] is False
