from fastapi import APIRouter, Depends

from app.middleware.auth_middleware import get_admin, login_required, get_current_user
from app.schemas.order_schema import OrderDTO
from app.services.order_service import (get_user_orders, 
                                        get_order, 
                                        get_all_orders_service, 
                                        delete_order_service, 
                                        create_new_order, 
                                        update_order_address)
from app.database import get_db
from app.repositories.user_repository import get_user_id_by_email

order_router = APIRouter()

@order_router.post("/orders")
async def create_order(order: OrderDTO, token:str = Depends(get_admin), db=Depends(get_db)):
    return create_new_order(order, db)

@order_router.post("/orders/me")
@login_required
async def create_user_order(order: OrderDTO, current_user: dict = Depends(get_current_user), db=Depends(get_db)):
    user_id = get_user_id_by_email(current_user.get("email"), db)
    order.user_id = user_id
    return create_new_order(order, db)

@order_router.get("/orders/{order_id}")
@login_required
async def get_order_by_orderid(order_id: int, current_user: dict = Depends(get_current_user), db=Depends(get_db)):
    return get_order(order_id, db)

@order_router.get("/orders/user/me")
@login_required
async def get_orders_by_user(current_user: dict = Depends(get_current_user), db=Depends(get_db)):
    user_id = get_user_id_by_email(current_user.get("email"), db)
    return get_user_orders(user_id, db)

@order_router.get("/orders")
async def show_orders(db=Depends(get_db), token = Depends(get_admin), limit: int = 10, offset: int = 0):
    return get_all_orders_service(db, limit, offset)

@order_router.delete("/orders/{order_id}")
@login_required
async def delete_order(order_id: int, current_user: dict = Depends(get_current_user), db=Depends(get_db)):
    return delete_order_service(order_id, db)


@order_router.patch("/orders/{order_id}")
@login_required
async def update_order(order_id: int,address: str, current_user: dict = Depends(get_current_user), db=Depends(get_db)):

    return update_order_address(order_id, address, db)