from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


class Item(BaseModel):
    id: Optional[int] = Field(None, description="The ID of the item")
    name: str = Field(..., description="The name of the item")
    description: Optional[str] = Field(None, description="A brief description of the item")
    price: float = Field(..., description="The price of the item")
    is_active: Optional[bool] = Field(True, description="Whether the item is active")
    created_at: Optional[datetime] = Field(None, description="The date and time the item was created")
    updated_at: Optional[datetime] = Field(None, description="The date and time the item was last updated")
