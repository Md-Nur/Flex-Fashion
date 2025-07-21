from sqlmodel import SQLModel, Field, Relationship # type: ignore
from server.models.cart import Cart
from typing import Optional

class CartItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="cart.id")
    variant_id: int = Field(foreign_key="variant.id")
    quantity: int

    cart: Cart = Relationship(back_populates="items")

