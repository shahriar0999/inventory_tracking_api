from pydantic import BaseModel, EmailStr


class ProductBase(BaseModel):
    id: str
    name: str
    category: str
    quantity: int
    reorder_level: int