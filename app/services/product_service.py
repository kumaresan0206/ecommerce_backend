from app.utils.logger import logger
from app.repositories.product_repository import (add_product, 
                                            get_all_products, 
                                            get_product_by_id, 
                                            update_full_product, 
                                            update_product_stock, 
                                            update_product_price, 
                                            delete_product)
from app.exceptions.custom_exceptions import DatabaseException, NotFoundException

def create_product(product, db):

    try:
        add_product(product.name, product.description, product.price, product.stock, db)
        return {"success": True, "message": "Product added successfully"}
    except Exception as e:
        logger.error(f"Error occurred while adding product: {e}")
        raise DatabaseException("An error occurred while adding product")

def get_products(db, limit, offset):
    try:
        products = get_all_products(db, limit, offset)
        return {"success": True, "products": products}
    except Exception as e:
        logger.error(f"Error occurred while fetching products: {e}")
        raise DatabaseException("An error occurred while fetching products")

def get_product(product_id, db):
    try:
        product = get_product_by_id(product_id, db)
        if product:
            return {"success": True, "product": product}
        else:
            raise NotFoundException("Product not found")
    except Exception as e:
        logger.error(f"Error occurred while fetching product: {e}")
        raise DatabaseException("An error occurred while fetching product")

def update_product(product_id, product, db):
    try:
        if product.price is not None or product.stock is not None:
            # Get the current product details
            current_product = get_product_by_id(product_id, db)
            if not current_product:
                raise NotFoundException("Product not found")

            # Update the product details
            if product.price is not None:
                update_product_price(product_id, product.price, db)
            if product.stock is not None:
                update_product_stock(product_id, product.stock, db)
        return {"success": True, "message": "Product updated successfully"}
    except Exception as e:
        logger.error(f"Error occurred while updating product: {e}")
        raise DatabaseException("An error occurred while updating product")

def update_full_product_info(product_id, product, db):
    try:
        update_full_product(product_id, product.name, product.description, product.price, product.stock, db)
        return {"success": True, "message": "Product updated successfully"}
    except Exception as e:
        logger.error(f"Error occurred while updating full product info: {e}")
        raise DatabaseException("An error occurred while updating full product info")

def delete_product_by_id(product_id, db):
    try:
        delete_product(product_id, db)
        return {"success": True, "message": "Product deleted successfully"}
    except Exception as e:
        logger.error(f"Error occurred while deleting product: {e}")
        raise DatabaseException("An error occurred while deleting product")
    
