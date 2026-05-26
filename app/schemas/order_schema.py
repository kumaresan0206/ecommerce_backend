from pydantic import BaseModel, Field

class OrderDTO(BaseModel):
    user_id: int
    product_id: int
    quantity: int = Field(gt=0)
    address: str