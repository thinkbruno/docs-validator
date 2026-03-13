from .validator import validate
from .detect import detect

from .br.cpf import validate_cpf
from .br.cnpj import validate_cnpj
from .br.generators import generate_cpf, generate_cnpj

__version__ = "1.0.0"

__all__ = [
    "validate",
    "detect",
    "validate_cpf",
    "validate_cnpj",
    "generate_cpf",
    "generate_cnpj",
]
