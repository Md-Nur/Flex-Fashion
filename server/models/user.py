from typing import List, Optional
from enum import StrEnum, auto
from sqlmodel import SQLModel, Field, Relationship # type: ignore
from models.address import Address
from models.order import Order
from server.models.cart_item import Cart

class UserRole(StrEnum):
    CUSTOMER = auto()
    ADMIN = auto()
    
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    email: str = Field(index=True, unique=True, default=None) # optional
    phone: str = Field(...) # required for contact
    password_hash: str
    role: UserRole = Field(default=UserRole.CUSTOMER)

    addresses: List[Address] = Relationship(back_populates="user")
    orders: List[Order] = Relationship(back_populates="user")
    cart: Optional[Cart] = Relationship(back_populates="user")
