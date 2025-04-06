from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
import models, schemas
import database 

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)

# @router.get("/")
# def test():
#     return {"message": "api is working........"}

# add new product
@router.post("/")
def add_product(product: schemas.ProductBase, db: Session = Depends(database.get_db)):
    new_product = models.Products(
        **product.dict()
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
  