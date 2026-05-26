from psycopg2.extras import RealDictCursor
from fastapi import HTTPException, status

from app.utils.logger import logger

def get_user_by_email(email: str, connection):
    
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        
        return user
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while fetching user by email: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while fetching user data")

def insert_user(name: str, email: str, password: str, role: str, connection):
    
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("INSERT INTO users (name, email, password, role) VALUES (%s, %s, %s, %s)", (name, email, password, role))
        connection.commit()
        return True
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while inserting user: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while inserting user data")

def get_user_id_by_email(email: str, connection):
    try:
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        
        return user["id"] if user else None
    except Exception as e:
        connection.rollback()
        logger.error(f"Error occurred while fetching user ID: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while fetching user ID")

