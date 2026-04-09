import re

# =====================================================
# 🔤 BASE36 (ALFANUMÉRICO)
# =====================================================
CHAR_MAP = {
    **{str(i): i for i in range(10)},
    **{chr(i + 55): i for i in range(10, 36)},  # A=10 ... Z=35
}


def _char_value(c: str) -> int:
    return CHAR_MAP[c]


def _normalize_alphanumeric(doc: str) -> str:
    return re.sub(r"[^0-9A-Z]", "", doc.upper())


# =====================================================
# 🧮 CNPJ ALFANUMÉRICO (EXPERIMENTAL)
# =====================================================
def _calculate_digit(values, weights):
    total = sum(v * w for v, w in zip(values, weights))
    dv = 11 - (total % 11)
    return 0 if dv >= 10 else dv


def validate_cnpj_alphanumeric(cnpj: str) -> bool:
    cnpj = _normalize_alphanumeric(cnpj)

    if len(cnpj) != 14:
        return False

    if not re.match(r"^[0-9A-Z]{12}[0-9]{2}$", cnpj):
        return False

    values = [_char_value(c) for c in cnpj]

    w1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    w2 = [6] + w1

    dv1 = _calculate_digit(values[:12], w1)
    if values[12] != dv1:
        return False

    dv2 = _calculate_digit(values[:13], w2)
    return values[13] == dv2


# =====================================================
# 🔢 CNPJ NUMÉRICO
# =====================================================
def _normalize_numeric(doc: str) -> str:
    return re.sub(r"\D", "", doc)


def _validate_cnpj_numeric(cnpj: str) -> bool:
    if not re.match(r"^\d{14}$", cnpj):
        return False

    if cnpj == cnpj[0] * 14:
        return False

    nums = [int(d) for d in cnpj]

    w1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    w2 = [6] + w1

    s1 = sum(nums[i] * w1[i] for i in range(12))
    dv1 = 11 - (s1 % 11)
    dv1 = 0 if dv1 >= 10 else dv1

    s2 = sum(nums[i] * w2[i] for i in range(13))
    dv2 = 11 - (s2 % 11)
    dv2 = 0 if dv2 >= 10 else dv2

    return nums[12] == dv1 and nums[13] == dv2


# =====================================================
# 🆔 CPF
# =====================================================
def validate_cpf(cpf: str) -> bool:
    cpf = _normalize_numeric(cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    nums = [int(d) for d in cpf]

    for i in range(9, 11):
        value = sum((nums[j] * ((i + 1) - j)) for j in range(i))
        digit = ((value * 10) % 11) % 10
        if nums[i] != digit:
            return False

    return True


# =====================================================
# 🏢 CNPJ (API PRINCIPAL)
# =====================================================
def validate_cnpj(
    cnpj: str,
    validate_dv: bool = True,
    mode: str = "strict",  # strict | loose | experimental
) -> bool:
    cnpj = _normalize_alphanumeric(cnpj)

    if len(cnpj) != 14:
        return False

    is_alpha = bool(re.search(r"[A-Z]", cnpj))

    # LOOSE
    if mode == "loose":
        return bool(
            re.match(r"^\d{14}$", cnpj) or re.match(r"^[0-9A-Z]{12}[0-9]{2}$", cnpj)
        )

    # EXPERIMENTAL
    if mode == "experimental":
        if is_alpha:
            return validate_cnpj_alphanumeric(cnpj)
        return _validate_cnpj_numeric(cnpj)

    # STRICT
    if is_alpha:
        return bool(re.match(r"^[0-9A-Z]{12}[0-9]{2}$", cnpj))

    return _validate_cnpj_numeric(cnpj) if validate_dv else True


# =====================================================
# 🔍 DETECT
# =====================================================
def detect(document: str) -> dict:
    doc = _normalize_alphanumeric(document)

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


# =====================================================
# 🧠 VALIDATOR (API)
# =====================================================
def validate(document: str) -> dict:
    return detect(document)


# Alias
validate_document = validate


# =====================================================
# 🖥 CLI
# =====================================================
def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python docs_validator_all.py <document>")
        sys.exit(1)

    print(validate(sys.argv[1]))


if __name__ == "__main__":
    main()
