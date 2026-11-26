import sys
from pathlib import Path

from lab_02_01_json_processing.exceptions import OrderProcessingError
from lab_02_01_json_processing.json_reader import read_json
from lab_02_01_json_processing.order_processor import (
    calculate_order_total,
    calculate_total_sales,
    filter_by_status,
    generate_summary,
    get_unique_customers,
    group_sales_by_customer,
)
from lab_02_01_json_processing.validators import VALID_STATUSES, validate_orders

DEFAULT_FILE_PATH = Path(__file__).resolve().parents[2] / "data" / "orders.json"


def show_menu():
    """Display the available operations."""
    print("\n====================================")
    print("       AXITY PYTHON LABS")
    print("       Order Processing System")
    print("====================================")
    print("1. List all orders")
    print("2. Filter orders by status")
    print("3. Calculate total sales")
    print("4. Group sales by customer")
    print("5. Show unique customers")
    print("6. Generate order summary")
    print("0. Exit")
    print("====================================")


def display_orders(orders):
    """Display a collection of orders."""

    if not orders:
        print("No orders found.")
        return

    for order in orders:
        total = calculate_order_total(order)

        print(
            f"ID: {order['id']} | "
            f"Customer: {order['customer']} | "
            f"Product: {order['product']} | "
            f"Status: {order['status']} | "
            f"Total: ${total:,.2f}"
        )


def display_summary(orders):
    """Display order statistics."""

    summary = generate_summary(orders)

    print("\n=== ORDER SUMMARY ===")
    print(f"Total orders: {summary['total_orders']}")
    print(f"Unique customers: {summary['unique_customers']}")
    print(f"Total amount: ${summary['total_amount']:,.2f}")
    print(f"Completed sales: ${summary['completed_sales']:,.2f}")
    print(f"Average order: ${summary['average_order']:,.2f}")
    print(f"Minimum order: ${summary['minimum_order']:,.2f}")
    print(f"Maximum order: ${summary['maximum_order']:,.2f}")

    print("\nOrders by status:")

    for status, count in summary["orders_by_status"].items():
        print(f"  {status}: {count}")


def run_menu(orders):
    """Execute the interactive menu."""

    while True:
        show_menu()

        option = input("Select an option: ").strip()

        try:
            match option:
                case "1":
                    display_orders(orders)

                case "2":
                    print(f"Available statuses: {', '.join(VALID_STATUSES)}")

                    status = input("Enter status: ").strip().lower()

                    if status not in VALID_STATUSES:
                        print("Invalid status.")
                        continue

                    filtered_orders = filter_by_status(orders, status)
                    display_orders(filtered_orders)

                case "3":
                    total = calculate_total_sales(orders)
                    print(f"\nTotal completed sales: ${total:,.2f}")

                case "4":
                    sales = group_sales_by_customer(orders)

                    print("\n=== SALES BY CUSTOMER ===")

                    for customer, total in sales.items():
                        print(f"{customer}: ${total:,.2f}")

                case "5":
                    customers = sorted(get_unique_customers(orders))

                    print("\n=== UNIQUE CUSTOMERS ===")

                    for index, customer in enumerate(customers, start=1):
                        print(f"{index}. {customer}")

                case "6":
                    display_summary(orders)

                case "0":
                    print("Goodbye!")
                    break

                case _:
                    print("Invalid option. Please try again.")

        except OrderProcessingError as error:
            print(f"Operation error: {error}")


def main():
    """Application entry point."""

    file_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_FILE_PATH

    try:
        orders = read_json(file_path)
        orders = validate_orders(orders)

        print(f"Successfully loaded {len(orders)} orders.")

        run_menu(orders)

    except OrderProcessingError as error:
        print(f"Application error: {error}", file=sys.stderr)
        return 1

    except (KeyboardInterrupt, EOFError):
        print("\nApplication interrupted.")
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
