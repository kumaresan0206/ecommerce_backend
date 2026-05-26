from app.repositories.cart_repository import (add_to_cart, 
                                            get_cart_items_by_user_id, 
                                            delete_cart_item)
from app.utils.logger import logger
from app.exceptions.custom_exceptions import DatabaseException

def add_item_to_cart(user_id, product_id, quantity, db):
    try:
        add_to_cart(user_id, product_id, quantity, db)
        return {"success": True, "message": "Item added to cart successfully"}
    except Exception as e:
        logger.error(f"Error occurred while adding item to cart: {e}")
        raise DatabaseException("An error occurred while adding item to cart")

def get_cart_items(user_id, db):
    try:
        cart_items = get_cart_items_by_user_id(user_id, db)
        return {"success": True, "cart_items": cart_items}
    except Exception as e:
        logger.error(f"Error occurred while fetching cart items: {e}")
        raise DatabaseException("An error occurred while fetching cart items")

def remove_cart_item(cart_id, db):
    try:
        delete_cart_item(cart_id, db)
        return {"success": True, "message": "Item removed from cart successfully"}
    except Exception as e:
        logger.error(f"Error occurred while removing cart item: {e}")
        raise DatabaseException("An error occurred while removing cart item")