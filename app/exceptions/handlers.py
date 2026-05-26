# app/exceptions/handlers.py

from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.exceptions.custom_exceptions import AppException
from app.utils.logger import logger


async def app_exception_handler(
    request: Request,
    exc: AppException
):

    logger.warning(
        f"""
        AppException:
        URL: {request.url}
        Message: {exc.message}
        """
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
            "errors": exc.errors
        }
    )


async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):

    formatted_errors = []

    for error in exc.errors():

        formatted_errors.append({
            "field": error["loc"][-1],
            "message": error["msg"]
        })

    logger.warning(
        f"""
        Validation Error:
        URL: {request.url}
        Errors: {formatted_errors}
        """
    )

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation failed",
            "errors": formatted_errors
        }
    )


async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.error(
        f"""
        Unhandled Exception:
        URL: {request.url}
        Error: {str(exc)}
        """
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error"
        }
    )