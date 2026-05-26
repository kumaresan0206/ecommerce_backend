from app.repositories.order_repository import (get_orders_by_user_id, 
                                            get_order_by_id, 
                                            get_all_orders, 
                                            delete_order, 
                                            place_order,
                                            update_order)
from app.utils.logger import logger
from app.exceptions.custom_exceptions import DatabaseException, NotFoundException

def create_new_order(order, db):
    try:
        place_order(order.user_id, order.product_id, order.quantity, order.address, db)
        return {"success": True, "message": "Order placed successfully"}
    except Exception as e:
        logger.error(f"Error occurred while placing order: {e}")
        raise DatabaseException("An error occurred while placing order")

def get_user_orders(user_id, db):
    try:
        orders = get_orders_by_user_id(user_id, db)
        return {"success": True, "orders": orders}
    except Exception as e:
        logger.error(f"Error occurred while fetching user orders: {e}")
        raise DatabaseException("An error occurred while fetching user orders")

def get_order(order_id, db):
    try:
        order = get_order_by_id(order_id, db)
        if order:
            return {"success": True, "order": order}
        else:
            raise NotFoundException("Order not found")
    except Exception as e:
        logger.error(f"Error occurred while fetching order: {e}")
        raise DatabaseException("An error occurred while fetching order")

def get_all_orders_service(db, limit, offset):
    try:
        orders = get_all_orders(db, limit, offset)
        return {"success": True, "orders": orders}
    except Exception as e:
        logger.error(f"Error occurred while fetching all orders: {e}")
        raise DatabaseException("An error occurred while fetching all orders")

def delete_order_service(order_id, db):
    try:
        delete_order(order_id, db)
        return {"success": True, "message": "Order deleted successfully"}
    except Exception as e:
        logger.error(f"Error occurred while deleting order: {e}")
        raise DatabaseException("An error occurred while deleting order")

def update_order_address(order_id, address, db):

    try:
        update_order(order_id, address, db)
        return {"success": True, "message": "Order updated successfully"}
    except Exception as e:
        logger.error(f"Error occurred while updating order address: {e}")
        raise DatabaseException("An error occurred while updating order address")