from fastapi import APIRouter, Depends
from app.middleware.auth_middleware import login_required, get_current_user
from app.schemas.cart_schema import CartDTO, CartItem
from app.database import get_db
from app.services.cart_service import add_item_to_cart, get_cart_items, remove_cart_item
from app.repositories.user_repository import get_user_id_by_email

cart_router = APIRouter()

@cart_router.post("/cart")
@login_required
async def add_to_cart(order: CartItem, current_user: str = Depends(get_current_user), db=Depends(get_db)):
    user_id = get_user_id_by_email(current_user.get("email"), db)
    order.user_id = user_id
    return add_item_to_cart(order, db)

@cart_router.get("/cart", response_model=CartDTO)
@login_required
async def get_cart(current_user: dict = Depends(get_current_user), db=Depends(get_db)):
    user_id = get_user_id_by_email(current_user.get("email"), db)
    return get_cart_items(user_id, db)

@cart_router.delete("/cart/{order_id}")
@login_required
async def delete_from_cart(order_id: int, current_user: dict = Depends(get_current_user), db=Depends(get_db)):
    return remove_cart_item(order_id, db)