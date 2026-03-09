import re


def normalize(value: str) -> str:
    """
    Remove non alphanumeric characters and uppercase value
    """
    return re.sub(r"[^A-Z0-9]", "", value.upper())


def char_to_value(char: str) -> int:
    """
    Convert alphanumeric character to numeric value
    """
    if char.isdigit():
        return int(char)

    return ord(char) - 55  # A=10 ... Z=35
