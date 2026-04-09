import sys

from docs_validator.cli import main


def test_cli_with_cnpj(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["prog", "11222333000181"])

    try:
        main()
    except SystemExit:
        pass


def test_cli_with_invalid(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["prog", "ABC"])

    try:
        main()
    except SystemExit:
        pass


def test_cli_output(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["prog", "11222333000181"])

    try:
        main()
    except SystemExit:
        pass

    captured = capsys.readouterr()

    assert captured.out != ""
