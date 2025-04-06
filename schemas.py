from pydantic import BaseModel, EmailStr


class ProductBase(BaseModel):
    # id: int
    name: str
    category: str
    quantity: int
    reorder_level: int