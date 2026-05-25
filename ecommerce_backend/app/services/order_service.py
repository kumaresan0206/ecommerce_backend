from app.repositories.order_repository import (get_orders_by_user_id, 
                                            get_order_by_id, 
                                            get_all_orders, 
                                            delete_order, 
                                            place_order)

def create_new_order(order, db):
    try:
        place_order(order.user_id, order.product_id, order.quantity, order.address, db)
        return {"success": True, "message": "Order placed successfully"}
    except Exception as e:
        return {"success": False, "message": str(e)}
    
def get_user_orders(user_id, db):
    try:
        orders = get_orders_by_user_id(user_id, db)
        return {"success": True, "orders": orders}
    except Exception as e:
        return {"success": False, "message": str(e)}

def get_order(order_id, db):
    try:
        order = get_order_by_id(order_id, db)
        if order:
            return {"success": True, "order": order}
        else:
            return {"success": False, "message": "Order not found"}
    except Exception as e:
        return {"success": False, "message": str(e)}
    
def get_all_orders_service(db, limit, offset):
    try:
        orders = get_all_orders(db, limit, offset)
        return {"success": True, "orders": orders}
    except Exception as e:
        return {"success": False, "message": str(e)}
    
def delete_order_service(order_id, db):
    try:
        delete_order(order_id, db)
        return {"success": True, "message": "Order deleted successfully"}
    except Exception as e:
        return {"success": False, "message": str(e)}