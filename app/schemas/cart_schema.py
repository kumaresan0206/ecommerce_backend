from pydantic import BaseModel, Field

class CartItemDTO(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class CartDTO(BaseModel):
    user_id: int
    items: list[CartItemDTO]
class CartResponseMessageDTO(BaseModel):
    success: bool
    message: str