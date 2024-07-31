from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    name: str
    description: Optional[str]
    price: int
    on_offer: Optional[float]


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
