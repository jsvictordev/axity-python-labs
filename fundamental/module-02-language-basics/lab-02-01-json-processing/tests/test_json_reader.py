import json

import pytest

from lab_02_01_json_processing.exceptions import (
    InvalidJsonError,
    OrderFileNotFoundError,
    OrderFileReadError,
)
from lab_02_01_json_processing.json_reader import read_json


def test_read_valid_json(tmp_path, sample_orders):
    # Arrange
    file_path = tmp_path / "orders.json"
    file_path.write_text(
        json.dumps(sample_orders),
        encoding="utf-8",
    )

    # Act
    result = read_json(file_path)

    # Assert
    assert result == sample_orders
    assert len(result) == 5


def test_read_empty_list(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.write_text("[]", encoding="utf-8")

    assert read_json(file_path) == []


def test_file_not_found(tmp_path):
    file_path = tmp_path / "missing.json"

    with pytest.raises(OrderFileNotFoundError):
        read_json(file_path)


def test_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text('{"id": 1001,', encoding="utf-8")

    with pytest.raises(InvalidJsonError):
        read_json(file_path)


def test_invalid_json_structure(tmp_path):
    file_path = tmp_path / "object.json"
    file_path.write_text('{"id": 1001}', encoding="utf-8")

    with pytest.raises(
        InvalidJsonError,
        match="The JSON root must be a list",
    ):
        read_json(file_path)


def test_invalid_file_encoding(tmp_path):
    file_path = tmp_path / "invalid_encoding.json"
    file_path.write_bytes(b"\xff\xfe\xff")

    with pytest.raises(InvalidJsonError):
        read_json(file_path)


def test_read_directory_as_file(tmp_path):
    with pytest.raises(OrderFileReadError):
        read_json(tmp_path)
