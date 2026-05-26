from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserLoginDTO, UserRegisterDTO, UserResponseDTO
from app.services.auth_service import register_user, login_user, get_current_user_info
from app.middleware.auth_middleware import get_current_user
from app.database import get_db
from app.middleware.auth_middleware import oauth2_scheme

auth_router = APIRouter()

@auth_router.post("/auth/register")
async def register(user: UserRegisterDTO, db=Depends(get_db)):
    return register_user(user, db)

@auth_router.post("/auth/login")
async def login(user: UserLoginDTO, db=Depends(get_db)):
    return  login_user(user, db)

@auth_router.get("/auth/me", response_model=UserResponseDTO)
async def get_user_detail(token: str = Depends(oauth2_scheme), db=Depends(get_db)):
    current_user = get_current_user(token)
    return get_current_user_info(current_user["email"], db)