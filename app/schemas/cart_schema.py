from pydantic import BaseModel, Field

class CartItem(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)

class CartDTO(BaseModel):
    user_id: int
    items: list[CartItem]