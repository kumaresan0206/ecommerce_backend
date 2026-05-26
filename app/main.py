from fastapi import FastAPI
from app.routes.auth_routes import auth_router
from app.routes.product_routes import product_router
from app.routes.order_routes import order_router
from app.routes.cart_routes import cart_router

app = FastAPI(title="E-commerce backend", version="1.0.0")

@app.get("/")
def home():
    return {"message": "E-commerce backend running"}

app.include_router(auth_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(cart_router)