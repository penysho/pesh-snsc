from django.core.exceptions import ObjectDoesNotExist


class AppException(Exception):
    """Base exception for the application."""

    pass


class NotFoundException(ObjectDoesNotExist):
    """Exception raised when object is not found."""

    pass


class DatabaseException(AppException):
    """Exception raised for database errors."""

    def __init__(self, error: Exception):
        super().__init__(f"Database error: {str(error)}")
