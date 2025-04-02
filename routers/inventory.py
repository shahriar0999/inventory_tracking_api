from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from inventory_tracking_api import models, schemas
from inventory_tracking_api.database import get_db

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

@router.get("/", )
def test():
    return {"message": "api is working........"}
  