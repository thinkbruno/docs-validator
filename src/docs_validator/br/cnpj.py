import re


def _normalize(cnpj: str) -> str:
    return re.sub(r"\D", "", cnpj)


def validate_cnpj(cnpj: str) -> bool:
    cnpj = _normalize(cnpj)

    if len(cnpj) != 14:
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
