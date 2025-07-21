from sqlmodel import SQLModel, Field, Relationship  # type: ignore
from typing import Optional, List
from models.category import Category  # Assuming Category is defined in models/category.py
from models.variant import Variant  # Assuming Variant is defined in models/variant.py
from models.review import Review  # Assuming Review is defined in models/review.py

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    base_price: float
    category_id: int = Field(foreign_key="category.id")
    image_url: Optional[str] = None

    category: Category = Relationship(back_populates="products")
    variants: List[Variant] = Relationship(back_populates="product")
    reviews: List[Review] = Relationship(back_populates="product")
