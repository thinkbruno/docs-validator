import re

# Base36: 0–9 + A–Z
CHAR_MAP = {
    **{str(i): i for i in range(10)},
    **{chr(i + 55): i for i in range(10, 36)},  # A=10 ... Z=35
}

CNPJ_ALPHANUMERIC_REGEX = re.compile(r"^[0-9A-Z]{12}[0-9]{2}$")


def normalize(doc: str) -> str:
    """
    Normaliza removendo caracteres inválidos e aplicando uppercase.
    """
    return re.sub(r"[^0-9A-Z]", "", doc.upper())


def char_value(c: str) -> int:
    """
    Converte caractere para valor base36.
    """
    if c not in CHAR_MAP:
        raise ValueError(f"Invalid character for CNPJ: {c}")
    return CHAR_MAP[c]


def _calculate_digit(values: list[int], weights: list[int]) -> int:
    """
    Calcula dígito verificador usando módulo 11 adaptado.
    """
    total = sum(v * w for v, w in zip(values, weights))
    dv = 11 - (total % 11)
    return 0 if dv >= 10 else dv


def validate_cnpj_alphanumeric(cnpj: str) -> bool:
    """
    EXPERIMENTAL

    Valida CNPJ alfanumérico incluindo dígitos verificadores.

    ATENÇÃO:
    Este algoritmo NÃO é oficial (até o momento).
    Pode ser alterado quando a Receita Federal definir a regra.
    """
    cnpj = normalize(cnpj)

    # valida estrutura (regra oficial)
    if not CNPJ_ALPHANUMERIC_REGEX.match(cnpj):
        return False

    try:
        values = [char_value(c) for c in cnpj]
    except ValueError:
        return False

    weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    weights2 = [6] + weights1

    dv1 = _calculate_digit(values[:12], weights1)
    if values[12] != dv1:
        return False

    dv2 = _calculate_digit(values[:13], weights2)
    return values[13] == dv2
