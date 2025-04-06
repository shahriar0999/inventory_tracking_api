from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
import models, schemas
import database 

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

# @router.get("/", )
# def test():
#     return {"message": "api is working........"}
  