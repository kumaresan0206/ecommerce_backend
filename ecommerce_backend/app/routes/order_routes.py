from fastapi import APIRouter, Depends
from app.schemas.order_schema import OrderDTO
from app.services.order_service import get_orders_by_user_id, get_order_by_id, get_all_orders_service, delete_order_service, place_order
from app.database import get_db

order_router = APIRouter()

@order_router.post("/orders")
async def create_order(order: OrderDTO, db=Depends(get_db)):
    return place_order(order, db)

@order_router.get("/orders/{order_id}")
async def get_order(order_id: int, db=Depends(get_db)):
    return get_order_by_id(order_id, db)

@order_router.get("/orders/user/{user_id}")
async def get_user_orders(user_id: int, db=Depends(get_db)):
    return get_orders_by_user_id(user_id, db)

@order_router.get("/orders")
async def show_orders(db=Depends(get_db), limit: int = 10, offset: int = 0):
    return get_all_orders_service(db, limit, offset)

@order_router.delete("/orders/{order_id}")
async def delete_order(order_id: int, db=Depends(get_db)):
    return delete_order_service(order_id, db)