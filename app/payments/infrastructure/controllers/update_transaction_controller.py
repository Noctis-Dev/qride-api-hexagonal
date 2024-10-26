from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.payments.infrastructure.repositories.sql_repository import SQLTransactionRepository
from app.payments.application.use_cases.update_transaction_use_case import UpdateTransactionUseCase
from app.payments.infrastructure.schemas import Transaction, TransactionUpdate
from app.db import get_db


class UpdateTransactionController:
    def __init__(self) -> None:
        self.use_case = UpdateTransactionUseCase()
        pass

    router = APIRouter()

    @router.put('/transactions/{transaction_uuid}', response_model=Transaction)
    def read_transaction(self, transaction_uuid: str, transactions_update: TransactionUpdate, db: Session = Depends(get_db)):
        transaction_repository = SQLTransactionRepository(db)
        self.use_case(transaction_repository)
        try:
            self.use_case.execute(transaction_uuid, commission=transactions_update.commission, description=transactions_update.description, transaction_date=transactions_update.date ,related_transaction_id=transactions_update.related_transaction_id)
            updated_transaction = transaction_repository.get(transaction_uuid)
            return updated_transaction
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))
