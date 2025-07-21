from sqlmodel import SQLModel, Field, Relationship  # type: ignore
from typing import Optional
from datetime import datetime
from models.product import Product  # Assuming Product is defined in models/product.py

class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    product_id: int = Field(foreign_key="product.id")
    rating: int = Field(ge=1, le=5)
    comment: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

    product: Product = Relationship(back_populates="reviews")

