from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str
    description: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

class ProductUpdate(BaseModel):
    price: float = Field(gt=0, default=None)
    stock: int = Field(ge=0, default=None)