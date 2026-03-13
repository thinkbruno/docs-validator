from docs_validator.br.cpf import validate_cpf


def test_valid_cpf():
    assert validate_cpf("52998224725")


def test_valid_formatted_cpf():
    assert validate_cpf("529.982.247-25")


def test_invalid_cpf():
    assert not validate_cpf("52998224726")


def test_repeated_digits():
    assert not validate_cpf("11111111111")
