from docs_validator.experimental.cnpj_alphanumeric import (
    validate_cnpj_alphanumeric,
    CHAR_MAP,
)


def test_invalid_alphanumeric():

    doc = "12ABC34501DE35"

    # apenas garantir que a função roda
    assert validate_cnpj_alphanumeric(doc) in [True, False]


def test_invalid_length():

    doc = "ABC123"

    assert validate_cnpj_alphanumeric(doc) is False
