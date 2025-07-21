from sqlmodel import SQLModel, Field, Relationship # type: ignore
from typing import Optional
from models.user import User  # Import User model for foreign key reference

class Address(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    country: str = "Bangladesh"
    city: str
    postal_code: str
    street_address: str
    is_primary: bool = False
    user: User = Relationship(back_populates="addresses")
