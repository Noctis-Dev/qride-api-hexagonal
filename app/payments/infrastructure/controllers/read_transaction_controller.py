from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.payments.infrastructure.repositories.sql_repository import SQLTransactionRepository
from app.payments.application.use_cases.read_transaction_use_case import ReadTransactionUseCase
from app.payments.infrastructure.schemas import Transaction
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

class ReadTransactionController:

    router = APIRouter()

    @router.get('/transactions/{transaction_uuid}', response_model=Transaction)
    def read_transaction(transaction_uuid: str, db: Session = Depends(get_db)):
        transaction_repository = SQLTransactionRepository(db)
        use_case = ReadTransactionUseCase(transaction_repository)
        try:
            transaction = use_case.execute(transaction_uuid)
            logging.info(f"read transaction ok: {transaction}")
            return transaction
        except ValueError as e:
            logging.error(f"could not read transaction: {e}")
            raise HTTPException(status_code=404, detail=str(e))