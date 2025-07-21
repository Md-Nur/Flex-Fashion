from datetime import datetime
from sqlmodel import SQLModel, Field # type: ignore

class Coupon(SQLModel, table=True):
    code: str = Field(primary_key=True)
    discount_percentage: float
    valid_until: datetime
    max_uses: int
    used_count: int = 0