import typer
from docs_validator import detect
from docs_validator.br.generators import generate_cpf, generate_cnpj
import json

app = typer.Typer()


@app.command()
def validate(doc: str):

    result = detect(doc)

    print(json.dumps(result, indent=2))


@app.command()
def generate(doc_type: str):

    if doc_type == "cpf":
        print(generate_cpf())

    elif doc_type == "cnpj":
        print(generate_cnpj())

    else:
        raise typer.BadParameter("doc_type must be cpf or cnpj")


if __name__ == "__main__":
    app()
