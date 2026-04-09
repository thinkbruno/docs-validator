import re

from docs_validator.br.cpf import validate_cpf
from docs_validator.br.cnpj import validate_cnpj


CPF_REGEX = re.compile(r"^\d{11}$")
CNPJ_NUMERIC_REGEX = re.compile(r"^\d{14}$")
CNPJ_ALPHANUMERIC_REGEX = re.compile(r"^[0-9A-Z]{12}[0-9]{2}$")


def normalize(document: str) -> str:
    """
    Normaliza documento:
    - mantém números e letras
    - converte para uppercase
    """
    return re.sub(r"[^0-9A-Z]", "", document.upper())


def detect(document: str):
    doc = normalize(document)

    # CPF
    if CPF_REGEX.match(doc):
        return {
            "country": "BR",
            "type": "CPF",
            "valid": validate_cpf(doc),
        }

    # numérico
    if CNPJ_NUMERIC_REGEX.match(doc):
        return {
            "country": "BR",
            "type": "CNPJ",
            "valid": validate_cnpj(doc),
        }

    # CNPJ alfa (novo)
    if CNPJ_ALPHANUMERIC_REGEX.match(doc):
        return {
            "country": "BR",
            "type": "CNPJ",
            "valid": validate_cnpj(doc),
        }

    return {
        "country": None,
        "type": None,
        "valid": False,
    }
