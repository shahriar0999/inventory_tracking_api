from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

@router.get("/", )
def test():
    return {"message": "api is working........"}
  