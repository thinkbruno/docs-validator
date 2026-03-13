# docs-validator

![CI](https://github.com/thinkbruno/docs-validator/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/github/license/thinkbruno/docs-validator)
![PyPI](https://img.shields.io/pypi/v/docs-validator)

A lightweight Python library for validating and generating document
numbers, starting with Brazilian documents.

The project focuses on:

- CPF validation
- CNPJ validation
- Experimental **alphanumeric CNPJ**
- Automatic document detection
- Document generators
- CLI usage
- PyPI distribution
- CI/CD and test coverage

---

# Installation

```bash
pip install docs-validator
```

For development:

```bash
git clone https://github.com/thinkbruno/docs-validator
cd docs-validator

python -m venv .venv
source .venv/bin/activate

pip install -e .
```

---

# Quick Usage

```python
from docs_validator import validate

validate("52998224725")
validate("11222333000181")
```

---

# API Overview

## Generic Validation

The `validate()` function automatically detects the document type.

```python
from docs_validator import validate

validate("52998224725")       # CPF
validate("11222333000181")    # CNPJ
```

---

## Auto Detection

```python
from docs_validator import detect

detect("52998224725")
detect("11222333000181")
detect("12ABC34501DE35")
```

Possible results:

    CPF
    CNPJ
    CNPJ_ALPHANUMERIC

---

# CPF Validation

```python
from docs_validator import validate_cpf

validate_cpf("52998224725")
```

---

# CNPJ Validation

```python
from docs_validator import validate_cnpj

validate_cnpj("11222333000181")
```

---

# Generators

Generate valid documents for testing environments.

```python
from docs_validator import generate_cpf, generate_cnpj

generate_cpf()
generate_cnpj()
```

Example:

    41799543807
    30167399000130

---

# Experimental: Alphanumeric CNPJ

Brazil's tax authority announced a future format allowing **alphanumeric
CNPJ identifiers**.

The library includes an experimental validator for this format.

```python
from docs_validator import validate

validate("12ABC34501DE35", mode="experimental")
```

⚠️ **Important**

As of 2026, no real alphanumeric CNPJs are publicly issued.

Any example used in tests or documentation is **synthetic** and only
intended to validate the algorithm.

---

# CLI Usage

After installation:

```bash
docs-validator validate 52998224725
docs-validator validate 11222333000181
```

Example output:

    VALID

---

# Testing

Run tests with:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=docs_validator
```

---

# Project Structure

    docs-validator
    │
    ├── src
    │   └── docs_validator
    │       ├── validator.py
    │       ├── detect.py
    │       │
    │       ├── br
    │       │   ├── cpf.py
    │       │   ├── cnpj.py
    │       │   └── generators.py
    │       │
    │       └── experimental
    │           └── cnpj_alphanumeric.py
    │
    ├── tests
    ├── README.md
    └── pyproject.toml

---

# Example Test Script

```python
from docs_validator import *

print(validate("52998224725"))
print(validate("11222333000181"))

print(detect("52998224725"))
print(detect("11222333000181"))

cpf = generate_cpf()
cnpj = generate_cnpj()

print(cpf, validate_cpf(cpf))
print(cnpj, validate_cnpj(cnpj))

print(validate("12ABC34501DE35", mode="experimental"))
```

---

# Why docs-validator?

Many validation libraries:

- focus only on regex
- do not implement real verification digit algorithms
- do not support future document formats

docs-validator focuses on:

- correctness of official validation algorithms
- simple and clean Python API
- extensibility for multiple countries

---

# Roadmap

Future goals for the library:

- Multi-country document validation
- Support for VAT / SSN style identifiers
- Additional generators
- Performance optimization
- Extended CLI capabilities

---

# Portfolio

Author portfolio:

https://thinkbruno.github.io/

---

# License

MIT License
