from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.payments.infrastructure.repositories.sql_repository import SQLTransactionRepository
from app.payments.application.use_cases.read_transaction_use_case import ReadTransactionUseCase
from app.payments.infrastructure.schemas import Transaction
from app.db import get_db

class ReadTransactionController:
    def __init__(self) -> None:
        self.use_case = ReadTransactionUseCase()
        pass

    router = APIRouter()

    @router.get('/transactions/{transaction_uuid}', response_model=Transaction)
    def read_transaction(self, transaction_uuid: str, db: Session = Depends(get_db)):
        transaction_repository = SQLTransactionRepository(db)
        self.use_case(transaction_repository)
        try:
            transaction = self.use_case.execute(transaction_uuid)
            return transaction
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))