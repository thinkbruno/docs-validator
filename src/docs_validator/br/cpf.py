import re


def _normalize(cpf: str) -> str:
    return re.sub(r"\D", "", cpf)


def validate_cpf(cpf: str) -> bool:
    cpf = _normalize(cpf)

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    nums = [int(d) for d in cpf]

    # primeiro DV
    total = sum(nums[i] * (10 - i) for i in range(9))
    dv1 = (total * 10 % 11) % 10

    # segundo DV
    total = sum(nums[i] * (11 - i) for i in range(10))
    dv2 = (total * 10 % 11) % 10

    return nums[9] == dv1 and nums[10] == dv2
