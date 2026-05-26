from fastapi import HTTPException, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from functools import wraps
from app.utils.jwt_handler import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_admin(token: str=Depends(oauth2_scheme)):
    payload = decode_access_token(token)

    if not payload or not payload.get("sub") or not payload.get("role"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    role = payload.get("role")

    if role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not an admin")

    return payload

def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        current_user = kwargs.get("current_user", None)
        if not current_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Login required")
        

        if  not current_user.get("email") or not current_user.get("role"):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")

        return func(*args, **kwargs)
    
    return wrapper

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)

    if not payload or not payload.get("sub") or not payload.get("role"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    email = payload.get("sub")
    role = payload.get("role")

    return {"email": email, "role": role}