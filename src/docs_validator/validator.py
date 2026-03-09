from .utils import normalize
from .dv import calculate_digit, WEIGHTS_FIRST, WEIGHTS_SECOND


def validate(cnpj: str) -> bool:
    cnpj = normalize(cnpj)

    if len(cnpj) != 14:
        return False

    base = cnpj[:12]
    dv = cnpj[12:]

    digit1 = calculate_digit(base, WEIGHTS_FIRST)
    digit2 = calculate_digit(base + str(digit1), WEIGHTS_SECOND)

    return dv == f"{digit1}{digit2}"
