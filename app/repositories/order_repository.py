from fastapi import HTTPException, status
from psycopg2.extras import RealDictCursor
from app.utils.logger import logger

def place_order(user_id: int, product_id: int, quantity: int, address: str, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("INSERT INTO orders (user_id, product_id, quantity, address) VALUES (%s, %s, %s, %s)", (user_id, product_id, quantity, address))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while placing order: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while placing order")

def get_orders_by_user_id(user_id: int, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM orders WHERE user_id = %s", (user_id,))
        orders = cursor.fetchall()
        return orders
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while fetching orders by user ID: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while fetching orders")

def get_all_orders(connection, limit, offset):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM orders LIMIT %s OFFSET %s", (limit, offset))
        orders = cursor.fetchall()
        return orders
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while fetching all orders: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while fetching orders")

def get_order_by_id(order_id: int, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM orders WHERE id = %s", (order_id,))
        order = cursor.fetchone()
        return order
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while fetching order by ID: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while fetching order data")

def delete_order(order_id: int, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while deleting order: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while deleting order data")

def update_order(order_id: int, address: str, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("UPDATE orders SET address = %s WHERE id = %s",
                       (address, order_id))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while updating order: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while updating order data")