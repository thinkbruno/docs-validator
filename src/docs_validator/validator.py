from docs_validator.detect import detect


def validate(document: str) -> dict:
    """
    Valida um documento brasileiro (CPF ou CNPJ).

    Esta é a função de mais alto nível da biblioteca.

    Args:
        document (str): Documento a ser validado

    Returns:
        dict: Estrutura com informações do documento:

        {
            "country": "BR" | None,
            "type": "CPF" | "CNPJ" | None,
            "valid": bool
        }
    """
    return detect(document)


# Alias público (API alternativa mais explícita)
validate_document = validate
