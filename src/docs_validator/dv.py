from .utils import char_to_value

WEIGHTS_FIRST = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
WEIGHTS_SECOND = [6] + WEIGHTS_FIRST


def calculate_digit(base: str, weights: list[int]) -> int:
    total = 0

    for char, weight in zip(base, weights):
        total += char_to_value(char) * weight

    remainder = total % 11

    return 0 if remainder < 2 else 11 - remainder
