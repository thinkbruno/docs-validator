import re

from docs_validator.br.cpf import validate_cpf
from docs_validator.br.cnpj import validate_cnpj


def normalize(doc: str) -> str:
    return re.sub(r"\D", "", doc)


def detect(document: str):

    doc = normalize(document)

    if len(doc) == 11:

        return {
            "country": "BR",
            "type": "CPF",
            "valid": validate_cpf(doc),
        }

    if len(doc) == 14:

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
