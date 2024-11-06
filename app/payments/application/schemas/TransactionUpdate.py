from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    user_id: int
    transaction_type: str
    amount: float
    commission: Optional[float] = 0.00
    description: Optional[str] = None
    related_transaction_id: Optional[int] = None

class TransactionUpdate(TransactionBase):
    date: datetime
    pass
