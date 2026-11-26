import math
import re

from lab_02_01_json_processing.exceptions import InvalidOrderError

VALID_STATUSES = ("completed", "pending", "cancelled")

REQUIRED_FIELDS = (
    "id",
    "customer",
    "email",
    "product",
    "quantity",
    "unit_price",
    "status",
)

EMAIL_PATTERN = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


def is_valid_email(email):
    """Validate the basic format of an email address."""
    return isinstance(email, str) and re.fullmatch(EMAIL_PATTERN, email) is not None


def validate_order(order):
    """Validate the structure and values of an order."""

    if not isinstance(order, dict):
        raise InvalidOrderError("Order must be a dictionary.")

    missing_fields = set(REQUIRED_FIELDS) - set(order)

    if missing_fields:
        raise InvalidOrderError(
            f"Missing required fields: {', '.join(sorted(missing_fields))}"
        )

    if type(order["id"]) is not int or order["id"] <= 0:
        raise InvalidOrderError("Order ID must be a positive integer.")

    if not isinstance(order["customer"], str) or not order["customer"].strip():
        raise InvalidOrderError("Customer must be a non-empty string.")

    if not is_valid_email(order["email"]):
        raise InvalidOrderError("Invalid email address.")

    if not isinstance(order["product"], str) or not order["product"].strip():
        raise InvalidOrderError("Product must be a non-empty string.")

    if type(order["quantity"]) is not int or order["quantity"] <= 0:
        raise InvalidOrderError("Quantity must be a positive integer.")

    price = order["unit_price"]

    if (
        type(price) not in (int, float)
        or price <= 0
        or (isinstance(price, float) and not math.isfinite(price))
    ):
        raise InvalidOrderError("Unit price must be a positive finite number.")

    if order["status"] not in VALID_STATUSES:
        raise InvalidOrderError(f"Invalid status. Allowed values: {VALID_STATUSES}")

    return order


def validate_orders(orders):
    """Validate a collection of orders."""

    if not isinstance(orders, list):
        raise InvalidOrderError("Orders must be a list.")

    validated_orders = []
    seen_ids = set()

    for index, order in enumerate(orders, start=1):
        try:
            validated_order = validate_order(order)

            order_id = validated_order["id"]

            if order_id in seen_ids:
                raise InvalidOrderError(f"Duplicate order ID: {order_id}")

            seen_ids.add(order_id)
            validated_orders.append(validated_order)

        except InvalidOrderError as error:
            raise InvalidOrderError(
                f"Invalid order at position {index}: {error}"
            ) from error

    return validated_orders
