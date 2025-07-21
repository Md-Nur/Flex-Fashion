from sqlmodel import SQLModel, Field, Relationship # type: ignore
from typing import Optional
from datetime import datetime

class Payment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id")
    amount: float
    method: str  # e.g., "bkash", "sslcommerz", "cod"
    transaction_id: Optional[str]
    paid_at: datetime = Field(default_factory=datetime.utcnow)
