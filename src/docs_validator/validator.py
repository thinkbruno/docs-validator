import re

from docs_validator.br.cpf import validate_cpf
from docs_validator.br.cnpj import validate_cnpj
from docs_validator.experimental.cnpj_alphanumeric import validate_cnpj_alphanumeric


def normalize(doc: str) -> str:
    """
    Remove caracteres não alfanuméricos.
    """
    return re.sub(r"[^0-9A-Za-z]", "", doc)


def detect(doc: str) -> str | None:
    """
    Detect document type automatically.

    Returns:
        CPF
        CNPJ
        CNPJ_ALPHANUMERIC
        None
    """

    doc = normalize(doc)

    if len(doc) == 11 and doc.isdigit():
        return "CPF"

    if len(doc) == 14:

        if doc.isdigit():
            return "CNPJ"

        if any(c.isalpha() for c in doc):
            return "CNPJ_ALPHANUMERIC"

    return None


def validate(doc: str, mode: str = "standard") -> bool:
    """
    Generic document validator.

    Parameters
    ----------
    doc : str
        Document number
    mode : str
        standard | experimental

    Returns
    -------
    bool
    """

    doc = normalize(doc)

    doc_type = detect(doc)

    if doc_type == "CPF":
        return validate_cpf(doc)

    if doc_type == "CNPJ":
        return validate_cnpj(doc)

    if doc_type == "CNPJ_ALPHANUMERIC":

        if mode == "experimental":
            return validate_cnpj_alphanumeric(doc)

        return False

    return False
