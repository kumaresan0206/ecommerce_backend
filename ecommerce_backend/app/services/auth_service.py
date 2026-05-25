from app.repositories.user_repository import get_user_by_email, insert_user
from app.utils.password_handler import hash_password, verify_password
from app.utils.jwt_handler import create_access_token

def register_user(user, db):

    existing_user = get_user_by_email(user.email, db)

    if existing_user:
        return {"success": False, "message": "User already exists"}
    
    hashed = hash_password(user.password)

    insert_user(user.name, user.email, hashed, "user", db)

    return {"success": True, "message": "User registered successfully"}

def login_user(user, db):
    
    existing_user = get_user_by_email(user.email, db)

    if not existing_user:
        return {"success": False, "message": "User doesn't exist"}
    
    if not verify_password(user.password, existing_user["password"]):
        return {"success": False, "message": "Incorrect password"}
    
    access_token = create_access_token({
        "sub": existing_user["email"],
        "role": existing_user["role"]
    })

    return {"success": True, "message": "User logged in successfully", "access_token": access_token}