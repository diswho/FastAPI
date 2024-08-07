from pydantic import BaseModel, Field

class Item(BaseModel):
    id: int = Field(..., ge=0)
    name: str
    description: str = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    is_active: bool = True
