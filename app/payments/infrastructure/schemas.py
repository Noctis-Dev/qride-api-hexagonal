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


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    date: datetime
    pass


class Transaction(TransactionBase):
    transaction_id: int

    class Config:
        orm_mode = True


class MPPaymentRequest(BaseModel):
    user_id: int
    price: float


class MPPaymentResponse(BaseModel):
    id: str
    init_point: str
    whatsapp_status: dict
