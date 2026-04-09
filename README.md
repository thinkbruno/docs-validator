# docs-validator

![CI](https://github.com/thinkbruno/docs-validator/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/github/license/thinkbruno/docs-validator)
![PyPI](https://img.shields.io/pypi/v/docs-validator)

A Python library and CLI to validate Brazilian documents (CPF, CNPJ), including experimental support for alphanumeric CNPJ.

## Features

- **Validate CPF**
- **Validate CNPJ** (numeric)
- **Experimental alphanumeric CNPJ**
- **Multiple validation modes:**
  - `strict` (default)
  - `loose`
  - `experimental`
- **CLI support**
- **JSON output**

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

# Usage

```python
from docs_validator import validate

result = validate("11222333000181")
print(result)
```

# Output

```json
{
  "country": "BR",
  "type": "CNPJ",
  "valid": true
}
```

---

# CLI Usage

## Basic

```python
docs-validator 11222333000181
```

## Force type

```python
docs-validator 12345678909 --type cpf
docs-validator 11222333000181 --type cnpj
```

## Modes

```python
docs-validator 12345678000100 --type cnpj --mode loose
docs-validator AB12CD34EF5601 --type cnpj --mode experimental
```

## Disable DV

```python
docs-validator 12345678000100 --type cnpj --no-dv
```

## Detect only

```python
docs-validator AB12CD34EF5601 --detect
```

## JSON Output

```python
docs-validator 11222333000181 --json
```

---

# Validation Modes

| Mode             | Description                            |
| :--------------- | :------------------------------------- |
| **strict**       | Safe default, validates DV for numeric |
| **loose**        | Only validates format                  |
| **experimental** | Enables alphanumeric DV validation     |

---

# Portfolio

## Author

Developed by [Bruno Ramos](https://www.brunoramos.tec.br)

---

# License

MIT License
