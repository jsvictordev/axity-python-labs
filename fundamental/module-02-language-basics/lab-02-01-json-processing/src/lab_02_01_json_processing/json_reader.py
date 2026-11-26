import json
from pathlib import Path

from lab_02_01_json_processing.exceptions import (
    InvalidJsonError,
    OrderFileNotFoundError,
    OrderFileReadError,
)


def read_json(file_path):
    """Read a JSON file and return its contents."""
    path = Path(file_path)

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError as error:
        raise OrderFileNotFoundError(f"File not found: {path}") from error

    except json.JSONDecodeError as error:
        raise InvalidJsonError(
            f"Invalid JSON at line {error.lineno}, " f"column {error.colno}"
        ) from error

    except UnicodeDecodeError as error:
        raise InvalidJsonError(f"Invalid file encoding: {path}") from error

    except OSError as error:
        raise OrderFileReadError(f"Unable to read file: {path}") from error

    if not isinstance(data, list):
        raise InvalidJsonError("The JSON root must be a list of orders.")

    return data
