from fastapi import FastAPI
from app.routes.auth_routes import auth_router
from app.routes.product_routes import product_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(product_router)

@app.get("/")
def home():
    return {"message": "E-commerce backend running"}