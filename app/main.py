from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from app.routes.auth_routes import auth_router
from app.routes.product_routes import product_router
from app.routes.order_routes import order_router
from app.routes.cart_routes import cart_router
from app.exceptions.handlers import (
    app_exception_handler,
    validation_exception_handler,
    global_exception_handler
)

from app.exceptions.custom_exceptions import AppException

app = FastAPI(title="E-commerce backend", version="1.0.0")

app.add_exception_handler(
    AppException,
    app_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

@app.get("/")
def home():
    return {"message": "E-commerce backend running"}

app.include_router(auth_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(cart_router)