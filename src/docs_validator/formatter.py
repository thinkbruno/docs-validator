from .utils import normalize


def format_cnpj(value: str) -> str:
    value = normalize(value)

    if len(value) != 14:
        raise ValueError("Invalid CNPJ length")

    return f"{value[:2]}.{value[2:5]}.{value[5:8]}/{value[8:12]}-{value[12:]}"
