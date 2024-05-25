from django.core.exceptions import ObjectDoesNotExist


class RepositoryException(Exception):
    """Base exception for the repositories."""

    pass


class NotFoundObjectException(ObjectDoesNotExist):
    """Exception raised when object is not found."""

    pass


class DatabaseException(RepositoryException):
    """Exception raised for database errors."""

    def __init__(self, error: Exception):
        super().__init__(f"Database error: {str(error)}")
