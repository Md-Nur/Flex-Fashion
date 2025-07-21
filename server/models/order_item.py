from pydantic import Field  # type: ignore
from sqlmodel import SQLModel, Relationship  # type: ignore
from models.order import Order  # Assuming Order model is defined in order.py
from typing import Optional

class OrderItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id")
    variant_id: int = Field(foreign_key="variant.id")
    quantity: int
    price_at_purchase: float

    order: Order = Relationship(back_populates="items")
