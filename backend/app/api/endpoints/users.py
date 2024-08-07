from fastapi import APIRouter, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.api.schemas import UserSchema, UserCreateSchema
from app.api.models import User
from app.database.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/{user_id}", response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user by ID.
    """
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

