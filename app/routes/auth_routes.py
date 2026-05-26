from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.schemas.user_schema import UserLogin, UserRegister
from app.services.auth_service import register_user, login_user
from app.utils.jwt_handler import decode_access_token
from app.database import get_db
from app.middleware.auth_middleware import oauth2_scheme

auth_router = APIRouter()

@auth_router.post("/auth/register")
async def register(user: UserRegister, db=Depends(get_db)):
    return register_user(user, db)

@auth_router.post("/auth/login")
async def login(user: UserLogin, db=Depends(get_db)):
    return  login_user(user, db)

@auth_router.get("/auth/me")
async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)

    if not payload or not payload.get("sub") or not payload.get("role"):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    email = payload.get("sub")
    role = payload.get("role")

    return {"email": email, "role": role}