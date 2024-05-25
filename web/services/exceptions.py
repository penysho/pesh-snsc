class SeviceException(Exception):
    """Base exception for the services."""

    pass


class SitePermissionException(SeviceException):
    """Exception raised when do not have permission for the target site."""

    def __init__(self):
        super().__init__("Do not have permission for the target site.")
