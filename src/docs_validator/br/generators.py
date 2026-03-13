import random


def generate_cpf():

    digits = [random.randint(0, 9) for _ in range(9)]

    total = sum(digits[i] * (10 - i) for i in range(9))
    dv1 = (total * 10 % 11) % 10
    digits.append(dv1)

    total = sum(digits[i] * (11 - i) for i in range(10))
    dv2 = (total * 10 % 11) % 10
    digits.append(dv2)

    return "".join(map(str, digits))


def generate_cnpj():

    base = [random.randint(0, 9) for _ in range(12)]

    w1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    w2 = [6] + w1

    s1 = sum(base[i] * w1[i] for i in range(12))
    dv1 = 11 - (s1 % 11)
    if dv1 >= 10:
        dv1 = 0

    base.append(dv1)

    s2 = sum(base[i] * w2[i] for i in range(13))
    dv2 = 11 - (s2 % 11)
    if dv2 >= 10:
        dv2 = 0

    base.append(dv2)

    return "".join(map(str, base))
