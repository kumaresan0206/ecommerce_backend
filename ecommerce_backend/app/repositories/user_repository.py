from psycopg2.extras import RealDictCursor

def get_user_by_email(email: str, connection):
    
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        
        return user
    except Exception as e:
        connection.rollback()
        raise e

def insert_user(name: str, email: str, password: str, role: str, connection):
    
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)", (name, email, password, role))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        raise e
    

