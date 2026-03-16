import re

CHAR_MAP = {
    **{str(i): i for i in range(10)},
    **{chr(i + 55): i for i in range(10, 36)},  # A=10 ... Z=35
}


def normalize(doc: str) -> str:
    return re.sub(r"[^0-9A-Z]", "", doc.upper())


def char_value(c: str) -> int:
    return CHAR_MAP[c]


def calculate_digit(values, weights):

    total = sum(v * w for v, w in zip(values, weights))

    dv = 11 - (total % 11)

    if dv >= 10:
        dv = 0

    return dv


def validate_cnpj_alphanumeric(cnpj: str) -> bool:

    cnpj = normalize(cnpj)

    if len(cnpj) != 14:
        return False

    values = [char_value(c) for c in cnpj]

    weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    weights2 = [6] + weights1

    dv1 = calculate_digit(values[:12], weights1)

    if values[12] != dv1:
        return False

    dv2 = calculate_digit(values[:13], weights2)

    return values[13] == dv2
