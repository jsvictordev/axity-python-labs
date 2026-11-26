import pytest

from lab_02_01_json_processing.exceptions import InvalidOrderError
from lab_02_01_json_processing.order_processor import (
    calculate_order_total,
    calculate_total_sales,
    count_orders_by_status,
    filter_by_status,
    generate_summary,
    get_unique_customers,
    group_sales_by_customer,
)


@pytest.mark.parametrize(
    "status,expected_count",
    [
        ("completed", 3),
        ("pending", 1),
        ("cancelled", 1),
    ],
)
def test_filter_by_status(sample_orders, status, expected_count):
    result = filter_by_status(sample_orders, status)

    assert len(result) == expected_count
    assert all(order["status"] == status for order in result)


def test_filter_invalid_status(sample_orders):
    with pytest.raises(InvalidOrderError):
        filter_by_status(sample_orders, "unknown")


def test_calculate_order_total(valid_order):
    assert calculate_order_total(valid_order) == 30000


def test_calculate_total_sales(sample_orders):
    assert calculate_total_sales(sample_orders) == 36000


def test_group_sales_by_customer(sample_orders):
    result = group_sales_by_customer(sample_orders)

    assert result == {
        "Juan Perez": 32400,
        "Maria Lopez": 3600,
    }


def test_get_unique_customers(sample_orders):
    result = get_unique_customers(sample_orders)

    assert result == {
        "Juan Perez",
        "Maria Lopez",
        "Carlos Garcia",
    }


def test_count_orders_by_status(sample_orders):
    result = count_orders_by_status(sample_orders)

    assert result == {
        "completed": 3,
        "pending": 1,
        "cancelled": 1,
    }


def test_generate_summary(sample_orders):
    result = generate_summary(sample_orders)

    assert result["total_orders"] == 5
    assert result["unique_customers"] == 3
    assert result["total_amount"] == 52000
    assert result["completed_sales"] == 36000
    assert result["average_order"] == 10400
    assert result["minimum_order"] == 2400
    assert result["maximum_order"] == 30000


def test_generate_empty_summary():
    result = generate_summary([])

    assert result["total_orders"] == 0
    assert result["unique_customers"] == 0
    assert result["total_amount"] == 0
    assert result["completed_sales"] == 0
    assert result["average_order"] == 0
    assert result["minimum_order"] == 0
    assert result["maximum_order"] == 0


def test_calculate_empty_sales():
    assert calculate_total_sales([]) == 0
