from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.payments.infrastructure.repositories.sql_repository import SQLTransactionRepository
from app.payments.application.use_cases.create_transaction_use_case import CreateTransactionUseCase
from app.payments.infrastructure.schemas import TransactionCreate, Transaction
from app.db import get_db

class CreateTransactionController:
    def __init__(self) -> None:
        self.use_case = CreateTransactionUseCase()
        pass
    
    router = APIRouter()
    
    @router.post('/transactions', response_model=Transaction)
    def create_transaction(self, transaction_create: TransactionCreate, db: Session = Depends(get_db)):
        transaction_repository = SQLTransactionRepository(db)
        self.use_case(transaction_repository)
        try:
            new_transaction = self.use_case.execute(
                user_id=transaction_create.user_id,
                transaction_type=transaction_create.transaction_type,
                amount=transaction_create.amount,
                commission=transaction_create.commission,
                description=transaction_create.description,
                related_transaction_id=transaction_create.related_transaction_id
            )
            return new_transaction
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail="Invalid transaction type or other integrity constraint violation")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))