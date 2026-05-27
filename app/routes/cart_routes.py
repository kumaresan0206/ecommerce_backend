from fastapi import APIRouter, Depends
from app.middleware.auth_middleware import login_required, get_current_user
from app.schemas.cart_schema import CartDTO, CartItemDTO, CartResponseMessageDTO
from app.database import get_db
from app.services.cart_service import add_item_to_cart, get_cart_items, remove_cart_item

cart_router = APIRouter()

@cart_router.post("/cart", response_model=CartResponseMessageDTO)
@login_required
async def add_to_cart(order: CartItemDTO, current_user: str = Depends(get_current_user), db=Depends(get_db)):
    return add_item_to_cart(current_user, order, db)

@cart_router.get("/cart", response_model=CartDTO)
@login_required
async def get_cart(current_user: dict = Depends(get_current_user), db=Depends(get_db)):
    return get_cart_items(current_user, db)

@cart_router.delete("/cart/{order_id}", response_model=CartResponseMessageDTO)
@login_required
async def delete_from_cart(order_id: int, current_user: dict = Depends(get_current_user), db=Depends(get_db)):
    return remove_cart_item(order_id, db)