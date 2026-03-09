# docs-validator

![CI](https://github.com/thinkbruno/docs-validator/actions/workflows/ci.yml/badge.svg?branch=main)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A lightweight Python library for validating Brazilian document
identifiers.

Currently the project supports:

- CNPJ (numeric)
- **Experimental support for alphanumeric CNPJ**

The project is designed with:

- clean architecture
- automated testing
- CI/CD
- PyPI-ready packaging

---

# ⚠️ About Alphanumeric CNPJ

As of **2026**, there are **no alphanumeric CNPJ numbers in public
circulation**.

The future format has been announced by the Receita Federal do Brasil,
but the official database still contains **only numeric CNPJ
identifiers**.

Therefore:

⚠️ Any alphanumeric CNPJ used in this project is **only for algorithm
testing purposes** and **does not represent a real company**.

---

# Experimental Validation Mode

To allow experimentation with the future format, the library supports an
**experimental validation mode**.

Example:

```python
from docs_validator import validate

validate("12ABC34501DE35", mode="experimental")
```

When using `mode="experimental"`:

- letters **A-Z** are allowed in the first 12 positions
- letters are converted using **base36 mapping**
- the **same modulo‑11 check digit algorithm** is applied

Mapping example:

    A = 10
    B = 11
    ...
    Z = 35

Without experimental mode:

```python
validate("12ABC34501DE35")
# returns False
```

---

# Installation

```bash
pip install docs-validator
```

---

# Usage

## Validate numeric CNPJ

```python
from docs_validator import validate

validate("11222333000181")
```

## Validate experimental alphanumeric CNPJ

```python
validate("12ABC34501DE35", mode="experimental")
```

## Format CNPJ

```python
from docs_validator import format_cnpj

format_cnpj("11222333000181")
```

Output:

    11.222.333/0001-81

---

# Running tests

```bash
pytest --cov=docs_validator
```

Generate HTML coverage report:

```bash
pytest --cov=docs_validator --cov-report=html
```

---

# Project structure

    docs-validator
    │
    ├── src/
    │   └── docs_validator/
    │
    ├── tests/
    │
    ├── pyproject.toml
    └── README.md

---

# Roadmap

Planned features:

- CPF validation
- document generators
- CLI interface
- support for additional Brazilian identifiers
- benchmarking tools

---

# Author

Bruno Ramos

LinkedIn\
https://www.linkedin.com/in/ramosbruno90/

GitHub\
https://github.com/thinkbruno

---

# License

MIT
