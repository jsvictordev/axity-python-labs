from lab_02_01_json_processing.exceptions import InvalidOrderError
from lab_02_01_json_processing.validators import VALID_STATUSES


def filter_by_status(orders, status):
    """Filter orders by status."""
    if status not in VALID_STATUSES:
        raise InvalidOrderError(f"Invalid status: {status}")

    return [order for order in orders if order["status"] == status]


def calculate_order_total(order):
    """Calculate the total amount of an order."""
    return order["quantity"] * order["unit_price"]


def calculate_total_sales(orders):
    """Calculate total sales from completed orders."""
    completed_orders = filter_by_status(orders, "completed")

    return sum(calculate_order_total(order) for order in completed_orders)


def group_sales_by_customer(orders):
    """Group completed sales by customer."""
    sales = {}

    for order in filter_by_status(orders, "completed"):
        customer = order["customer"]
        total = calculate_order_total(order)

        sales[customer] = sales.get(customer, 0) + total

    return sales


def get_unique_customers(orders):
    """Return unique customer names."""
    return {order["customer"] for order in orders}


def count_orders_by_status(orders):
    """Count orders for each valid status."""
    return {status: len(filter_by_status(orders, status)) for status in VALID_STATUSES}


def generate_summary(orders):
    """Generate a summary of order statistics."""
    totals = [calculate_order_total(order) for order in orders]

    return {
        "total_orders": len(orders),
        "unique_customers": len(get_unique_customers(orders)),
        "total_amount": sum(totals),
        "completed_sales": calculate_total_sales(orders),
        "average_order": sum(totals) / len(totals) if totals else 0,
        "minimum_order": min(totals, default=0),
        "maximum_order": max(totals, default=0),
        "orders_by_status": count_orders_by_status(orders),
    }
