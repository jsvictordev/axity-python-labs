class OrderProcessingError(Exception):
    """Base exception for order processing errors."""


class OrderFileNotFoundError(OrderProcessingError):
    """Raised when the orders file does not exist."""


class InvalidJsonError(OrderProcessingError):
    """Raised when the JSON file has an invalid format."""


class OrderFileReadError(OrderProcessingError):
    """Raised when the orders file cannot be read."""


class InvalidOrderError(OrderProcessingError):
    """Raised when an order contains invalid data."""
