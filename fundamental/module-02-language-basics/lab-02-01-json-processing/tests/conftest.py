import pytest


@pytest.fixture
def valid_order():
    return {
        "id": 1001,
        "customer": "Juan Perez",
        "email": "juan@example.com",
        "product": "Laptop",
        "quantity": 2,
        "unit_price": 15000,
        "status": "completed",
    }


@pytest.fixture
def sample_orders(valid_order):
    return [
        valid_order,
        {
            **valid_order,
            "id": 1002,
            "customer": "Maria Lopez",
            "email": "maria@example.com",
            "product": "Monitor",
            "quantity": 3,
            "unit_price": 4500,
            "status": "pending",
        },
        {
            **valid_order,
            "id": 1003,
            "product": "Keyboard",
            "quantity": 2,
            "unit_price": 1200,
        },
        {
            **valid_order,
            "id": 1004,
            "customer": "Carlos Garcia",
            "email": "carlos@example.com",
            "product": "Mouse",
            "quantity": 5,
            "unit_price": 500,
            "status": "cancelled",
        },
        {
            **valid_order,
            "id": 1005,
            "customer": "Maria Lopez",
            "email": "maria@example.com",
            "product": "Headphones",
            "quantity": 2,
            "unit_price": 1800,
        },
    ]
