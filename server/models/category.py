from sqlmodel import SQLModel, Field, Relationship # type: ignore
from typing import List
from product import Product  # Assuming Product is defined in product.py
from typing import Optional

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    products: List[Product] = Relationship(back_populates="category")

