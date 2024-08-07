from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.api.schemas import ItemSchema, ItemCreateSchema
from app.api.models import Item
from app.database.database import get_db

router = APIRouter(prefix="/items", tags=["items"])

@router.post("/", response_model=ItemSchema, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreateSchema, db: Session = Depends(get_db)):
    """
    Create a new item.
    """
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/{item_id}", response_model=ItemSchema)
def get_item(item_id: int, db: Session = Depends(get_db)):
    """
    Get an item by ID.
    """
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return db_item
