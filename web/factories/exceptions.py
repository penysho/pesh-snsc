class FactoryException(Exception):
    """Base exception for the factories."""

    pass


class NotFoundDependencyException(FactoryException):
    """Exception raised when dependencies are not found."""
