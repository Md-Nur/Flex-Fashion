from sqlmodel import SQLModel, Field, Relationship  # type: ignore
from typing import Optional
from models.product import Product  # Assuming Product is defined in models/product.py

class Variant(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    size: str
    color: str
    stock: int
    price: Optional[float] = None  # Override base_price if needed

    product: Product = Relationship(back_populates="variants")
