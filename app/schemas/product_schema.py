from pydantic import BaseModel, Field

class ProductDTO(BaseModel):
    name: str
    description: str
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

class ProductUpdateDTO(BaseModel):
    price: float = Field(gt=0, default=None)
    stock: int = Field(ge=0, default=None)

class SuccessResponseDTO(BaseModel):
    success: bool
    message: str = None

class ProductResponseDTO(BaseModel):
    success: bool
    product: ProductDTO = None