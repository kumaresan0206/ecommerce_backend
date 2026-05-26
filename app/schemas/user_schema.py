from pydantic import BaseModel, EmailStr, Field, field_validator

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str= Field(min_length=8)

    @field_validator("password")
    @classmethod
    def check_password(cls, v):

        if not any(char.isdigit() for char in v):
            raise ValueError("Password should contain at least one number")
        if not any(char.isupper() for char in v):
            raise ValueError("Password should contain at least one uppercase letter")
        if not any(char.islower() for char in v):
            raise ValueError("Password should contain at least one lowercase letter")
        if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>/?\\" for char in v):
            raise ValueError("Password should contain at least one special character")

        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str