# app/exceptions/custom_exceptions.py

class AppException(Exception):

    def __init__(
        self,
        message: str,
        status_code: int = 400,
        errors=None
    ):

        self.message = message
        self.status_code = status_code
        self.errors = errors


class NotFoundException(AppException):

    def __init__(
        self,
        message: str = "Resource not found"
    ):

        super().__init__(
            message=message,
            status_code=404
        )


class AuthenticationException(AppException):

    def __init__(
        self,
        message: str = "Authentication failed"
    ):

        super().__init__(
            message=message,
            status_code=401
        )


class AuthorizationException(AppException):

    def __init__(
        self,
        message: str = "Permission denied"
    ):

        super().__init__(
            message=message,
            status_code=403
        )


class ValidationException(AppException):

    def __init__(
        self,
        message: str = "Validation failed",
        errors=None
    ):

        super().__init__(
            message=message,
            status_code=422,
            errors=errors
        )


class DatabaseException(AppException):

    def __init__(
        self,
        message: str = "Database operation failed"
    ):

        super().__init__(
            message=message,
            status_code=500
        )