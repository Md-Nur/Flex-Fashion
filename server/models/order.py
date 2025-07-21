from pydantic import Field # type: ignore
from sqlmodel import SQLModel, Relationship # type: ignore
from typing import List, Optional
from enum import StrEnum, auto
from datetime import datetime
from models.user import User  # Assuming User model is defined in user.py
from models.order_item import OrderItem  # Assuming OrderItem model is defined in order_item.py

class OrderStatus(StrEnum):
    PENDING = auto()
    PAID = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()


class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    address_id: int = Field(foreign_key="address.id")
    total_amount: float
    status: OrderStatus = Field(default=OrderStatus.PENDING)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    coupon_code: Optional[str] = None
    discount: float = 0.0

    user: User = Relationship(back_populates="orders")
    items: List[OrderItem] = Relationship(back_populates="order")

