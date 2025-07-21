from sqlmodel import SQLModel, Field, Relationship  # type: ignore
from models.user import User
from models.cart_item import CartItem
from typing import List
from typing import Optional

class Cart(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")

    user: User = Relationship(back_populates="cart")
    items: List[CartItem] = Relationship(back_populates="cart")
