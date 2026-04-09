import sys
from docs_validator.validator import validate


def main():
    """
    CLI entrypoint.

    Usage:
        docs-validator <document>
    """
    if len(sys.argv) < 2:
        print("Usage: docs-validator <document>")
        sys.exit(1)

    document = sys.argv[1]

    result = validate(document)

    print(result)


if __name__ == "__main__":
    main()
