from docs_validator.br.generators import generate_cpf, generate_cnpj
from docs_validator.br.cpf import validate_cpf
from docs_validator.br.cnpj import validate_cnpj


def test_generate_cpf():
    cpf = generate_cpf()
    assert validate_cpf(cpf)


def test_generate_cnpj():
    cnpj = generate_cnpj()
    assert validate_cnpj(cnpj)
