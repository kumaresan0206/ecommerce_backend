from app.repositories.user_repository import get_user_by_email, insert_user, get_user_details_by_email
from app.utils.password_handler import hash_password, verify_password
from app.utils.jwt_handler import create_access_token
from app.utils.logger import logger
from app.exceptions.custom_exceptions import AppException, DatabaseException, NotFoundException, AuthenticationException

def register_user(user, db):

    try:

        existing_user = get_user_by_email(user.email, db)

        if existing_user:
            raise AppException("User already exists")
        
        hashed = hash_password(user.password)

        insert_user(user.name, user.email, hashed, "user", db)

        return {"success": True, "message": "User registered successfully"}
    except Exception as e:
        logger.error(f"Error occurred during registration: {e}")
        raise DatabaseException("An error occurred during registration")
    

def login_user(user, db):

    try:
        existing_user = get_user_by_email(user.email, db)

        if not existing_user:
            raise NotFoundException("User doesn't exist")
        
        if not verify_password(user.password, existing_user["password"]):
            raise AuthenticationException("Incorrect password")
        
        access_token = create_access_token({
            "sub": existing_user["email"],
            "role": existing_user["role"]
        })

        return {"success": True, "message": "User logged in successfully", "access_token": access_token}
    except Exception as e:
        logger.error(f"Error occurred during login: {e}")
        raise DatabaseException("An error occurred during login")
    
def get_current_user_info(email, db):
    try:
        user = get_user_details_by_email(email, db)
        if user:
            return {"success": True, "name": user["name"], "email": user["email"], "role": user["role"]}
        else:
            raise NotFoundException("User not found")
    except Exception as e:
        logger.error(f"Error occurred while fetching user info: {e}")
        raise DatabaseException("An error occurred while fetching user info")