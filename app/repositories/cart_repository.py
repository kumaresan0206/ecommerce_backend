from psycopg2.extras import RealDictCursor

from app.utils.logger import logger
from app.exceptions.custom_exceptions import DatabaseException

def add_to_cart(user_id: int, product_id: int, quantity: int, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("INSERT INTO cart (user_id, product_id, quantity) VALUES (%s, %s, %s)", (user_id, product_id, quantity))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while adding to cart: {e}")
        raise DatabaseException("An error occurred while adding to cart")

def get_cart_items_by_user_id(user_id: int, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM cart WHERE user_id = %s", (user_id,))
        cart_items = cursor.fetchall()
        return cart_items
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while fetching cart items: {e}")
        raise DatabaseException("An error occurred while fetching cart items")

def delete_cart_item(cart_id: int, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("DELETE FROM cart WHERE id = %s", (cart_id,))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while deleting cart item: {e}")
        raise DatabaseException("An error occurred while deleting cart item")