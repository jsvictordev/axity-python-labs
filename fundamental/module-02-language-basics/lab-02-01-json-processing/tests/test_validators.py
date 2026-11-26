import pytest

from lab_02_01_json_processing.exceptions import InvalidOrderError
from lab_02_01_json_processing.validators import (
    is_valid_email,
    validate_order,
    validate_orders,
)


@pytest.mark.parametrize(
    "email,expected",
    [
        ("juan@example.com", True),
        ("user.name@gmail.com", True),
        ("user+test@example.com.mx", True),
        ("invalid-email", False),
        ("user@domain", False),
        ("user@@example.com", False),
        ("", False),
        (None, False),
    ],
)
def test_email_validation(email, expected):
    assert is_valid_email(email) is expected


def test_validate_valid_order(valid_order):
    result = validate_order(valid_order)

    assert result == valid_order


@pytest.mark.parametrize(
    "field,value",
    [
        ("id", -1),
        ("id", True),
        ("customer", ""),
        ("email", "invalid-email"),
        ("product", ""),
        ("quantity", -5),
        ("quantity", True),
        ("unit_price", 0),
        ("status", "unknown"),
    ],
)
def test_validate_invalid_order(valid_order, field, value):
    valid_order[field] = value

    with pytest.raises(InvalidOrderError):
        validate_order(valid_order)


def test_missing_required_field(valid_order):
    del valid_order["customer"]

    with pytest.raises(
        InvalidOrderError,
        match="Missing required fields",
    ):
        validate_order(valid_order)


def test_validate_orders(sample_orders):
    result = validate_orders(sample_orders)

    assert result == sample_orders
    assert len(result) == 5


def test_duplicate_order_id(sample_orders):
    sample_orders.append(sample_orders[0].copy())

    with pytest.raises(
        InvalidOrderError,
        match="Duplicate order ID",
    ):
        validate_orders(sample_orders)
