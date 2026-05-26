from fastapi import HTTPException, status

from app.repositories.user_repository import get_user_by_email, insert_user
from app.utils.password_handler import hash_password, verify_password
from app.utils.jwt_handler import create_access_token
from app.utils.logger import logger

def register_user(user, db):

    try:

        existing_user = get_user_by_email(user.email, db)

        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
        
        hashed = hash_password(user.password)

        insert_user(user.name, user.email, hashed, "user", db)

        return {"success": True, "message": "User registered successfully"}
    except Exception as e:
        logger.error(f"Error occurred during registration: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred during registration")
    

def login_user(user, db):

    try:
        existing_user = get_user_by_email(user.email, db)

        if not existing_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User doesn't exist")
        
        if not verify_password(user.password, existing_user["password"]):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
        
        access_token = create_access_token({
            "sub": existing_user["email"],
            "role": existing_user["role"]
        })

        return {"success": True, "message": "User logged in successfully", "access_token": access_token}
    except Exception as e:
        logger.error(f"Error occurred during login: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred during login")