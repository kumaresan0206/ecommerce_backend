from psycopg2.extras import RealDictCursor

def add_product(name: str, description: str, price: float, stock: int, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("INSERT INTO products (name, description, price, stock) VALUES (%s, %s, %s, %s)", (name, description, price, stock))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        raise e
    
def get_all_products(connection, limit, offset):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM products LIMIT %s OFFSET %s", (limit, offset))
        products = cursor.fetchall()
        return products
    except Exception as e:
        raise e
    
def get_product_by_id(product_id: int, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM products WHERE id = %s", (product_id,))
        product = cursor.fetchone()
        return product
    except Exception as e:
        raise e
    
def update_full_product(product_id: int, name: str, description: str, price: float, stock: int, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("UPDATE products SET name = %s, description = %s, price = %s, stock = %s WHERE id = %s", (name, description, price, stock, product_id))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        raise e
    

def update_product_stock(product_id: int, stock: int, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("UPDATE products SET stock = %s WHERE id = %s", (stock, product_id))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        raise e
    
def update_product_price(product_id: int, price: float, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("UPDATE products SET price = %s WHERE id = %s", (price, product_id))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        raise e
    
def delete_product(product_id: int, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        raise e