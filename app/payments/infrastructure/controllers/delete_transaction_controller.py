from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.payments.infrastructure.repositories.sql_repository import SQLTransactionRepository
from app.payments.application.use_cases.delete_transaction_use_case import DeleteTransactionUseCase
from app.payments.infrastructure.schemas import TransactionCreate, Transaction
from app.db import get_db


class DeleteTransactionController:
    def __init__(self) -> None:
        self.use_case = DeleteTransactionUseCase()
        pass
    
    router = APIRouter

    @router.delete('/transactions/{transaction_uuid}', response_model=Transaction)
    def delete_transaction(self, transaction_uuid: int, db: Session = Depends(get_db)):
        transaction_repository = SQLTransactionRepository(db)
        self.use_case(transaction_repository)
        
        try:
            
            transaction_to_delete = transaction_repository.get(transaction_uuid)
            if not transaction_to_delete:
                raise HTTPException(status_code=404, detail="Transaction not found")
            
            self.use_case.execute(transaction_id=transaction_uuid)
            
            return transaction_to_delete 
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail="Could not delete the transaction due to integrity constraints")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))