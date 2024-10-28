from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.payments.infrastructure.repositories.sql_repository import SQLTransactionRepository
from app.payments.application.use_cases.create_transaction_use_case import CreateTransactionUseCase
from app.payments.infrastructure.schemas import TransactionCreate, Transaction
from app.db import get_db
import logging
import os

log_dir = "var/log"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, 'myapp.log'), 
    level=logging.INFO,                             
    format='%(asctime)s - %(levelname)s - %(message)s'  
)

class CreateTransactionController:
    
    router = APIRouter()
    
    @router.post('/transactions', response_model=Transaction)
    def create_transaction(transaction_create: TransactionCreate, db: Session = Depends(get_db)):
        transaction_repository = SQLTransactionRepository(db)
        use_case = CreateTransactionUseCase(transaction_repository)
        try:
            new_transaction = use_case.execute(
                user_id=transaction_create.user_id,
                transaction_type=transaction_create.transaction_type,
                amount=transaction_create.amount,
                commission=transaction_create.commission,
                description=transaction_create.description,
                related_transaction_id=transaction_create.related_transaction_id
            )
            logging.info(f"Transaction created: {new_transaction}")
            return new_transaction
        except IntegrityError as e:
            db.rollback()
            logging.error(f"Could not create transaction due to integrity constraints: {str(e)}")
            raise HTTPException(status_code=400, detail="Invalid transaction type or other integrity constraint violation")
        except ValueError as e:
            logging.error(f"Could not create transaction: {str(e)}")
            raise HTTPException(status_code=400, detail=str(e))