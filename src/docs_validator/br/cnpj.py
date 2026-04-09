import re

from docs_validator.experimental.cnpj_alphanumeric import (
    validate_cnpj_alphanumeric,
)

CNPJ_NUMERIC_REGEX = re.compile(r"^\d{14}$")
CNPJ_ALPHANUMERIC_REGEX = re.compile(r"^[0-9A-Z]{12}[0-9]{2}$")


def _normalize(cnpj: str) -> str:
    return re.sub(r"[^0-9A-Z]", "", cnpj.upper())


def _is_alphanumeric(cnpj: str) -> bool:
    return bool(re.search(r"[A-Z]", cnpj))


def validate_cnpj(
    cnpj: str,
    validate_dv: bool = True,
    strict: bool = True,
    mode: str = "strict",
) -> bool:
    """
    Valida CNPJ com suporte a múltiplos modos.

    mode:
        - "strict": padrão seguro (recomendado)
        - "loose": apenas formato
        - "experimental": inclui DV alfanumérico

    validate_dv:
        controla validação de DV (quando aplicável)

    strict:
        compatibilidade com versões anteriores
    """

    cnpj = _normalize(cnpj)

    if len(cnpj) != 14:
        return False

    is_alpha = _is_alphanumeric(cnpj)

    if mode == "loose":
        return _validate_format(cnpj)

    if mode == "experimental":
        if is_alpha:
            return validate_cnpj_alphanumeric(cnpj)
        return _validate_cnpj_numeric(cnpj) if validate_dv else _validate_format(cnpj)

    if is_alpha:
        # apenas estrutura oficial
        return _validate_cnpj_alphanumeric_structural(cnpj)

    # numérico
    if validate_dv:
        return _validate_cnpj_numeric(cnpj)

    return _validate_format(cnpj)


def _validate_format(cnpj: str) -> bool:
    return bool(CNPJ_NUMERIC_REGEX.match(cnpj) or CNPJ_ALPHANUMERIC_REGEX.match(cnpj))


def _validate_cnpj_numeric(cnpj: str) -> bool:
    if not CNPJ_NUMERIC_REGEX.match(cnpj):
        return False

    if cnpj == cnpj[0] * 14:
        return False

    nums = [int(d) for d in cnpj]

    w1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    w2 = [6] + w1

    s1 = sum(nums[i] * w1[i] for i in range(12))
    dv1 = 11 - (s1 % 11)
    if dv1 >= 10:
        dv1 = 0

    s2 = sum(nums[i] * w2[i] for i in range(13))
    dv2 = 11 - (s2 % 11)
    if dv2 >= 10:
        dv2 = 0

    return nums[12] == dv1 and nums[13] == dv2


def _validate_cnpj_alphanumeric_structural(cnpj: str) -> bool:
    return bool(CNPJ_ALPHANUMERIC_REGEX.match(cnpj))
