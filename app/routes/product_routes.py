from fastapi import APIRouter, Depends
from app.schemas.product_schema import ProductDTO, ProductUpdateDTO
from app.services.product_service import get_products, get_product, create_product, update_product, update_full_product_info, delete_product_by_id
from app.database import get_db
from app.middleware.auth_middleware import get_admin

product_router = APIRouter()

@product_router.post("/products")
async def add_product(product: ProductDTO, token: str = Depends(get_admin), db=Depends(get_db)):
    
    if isinstance(token, dict) and not token.get("success", True):
        return {"success": False, "message": token.get("message", "Unauthorized")}
    
    return create_product(product, db)

@product_router.get("/products", response_model=list[ProductDTO])
async def show_all_products(db=Depends(get_db), limit: int = 10, offset: int = 0):
    return get_products(db, limit, offset)

@product_router.get("/products/{product_id}")
async def show_product(product_id: int, db=Depends(get_db)):
    return get_product(product_id, db)

@product_router.put("/products/{product_id}")
async def update_product_info(product_id: int, product: ProductUpdateDTO, token: str = Depends(get_admin), db=Depends(get_db)):
    
    if isinstance(token, dict) and not token.get("success", True):
        return {"success": False, "message": token.get("message", "Unauthorized")}
    
    return update_product(product_id, product, db)

@product_router.delete("/products/{product_id}")
async def delete_product(product_id: int, token: str = Depends(get_admin), db=Depends(get_db)):
    
    if isinstance(token, dict) and not token.get("success", True):
        return {"success": False, "message": token.get("message", "Unauthorized")}
    
    return delete_product_by_id(product_id, db)

@product_router.patch("/products/{product_id}")
async def update_product_price_or_stock(product_id: int, product: ProductUpdateDTO, token: str = Depends(get_admin), db=Depends(get_db)):
    
    if isinstance(token, dict) and not token.get("success", True):
        return {"success": False, "message": token.get("message", "Unauthorized")}
    
    return update_product(product_id, product, db)

@product_router.put("/products/{product_id}")
async def update_full_product(product_id: int, product: ProductDTO, token: str = Depends(get_admin), db=Depends(get_db)):
    
    if isinstance(token, dict) and not token.get("success", True):
        return {"success": False, "message": token.get("message", "Unauthorized")}
    
    return update_full_product_info(product_id, product, db)