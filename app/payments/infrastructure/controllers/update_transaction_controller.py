from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.payments.infrastructure.repositories.sql_repository import SQLTransactionRepository
from app.payments.application.use_cases.update_transaction_use_case import UpdateTransactionUseCase
from app.payments.infrastructure.schemas import Transaction, TransactionUpdate
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

class UpdateTransactionController:
    
    router = APIRouter()

    @router.put('/transactions/{transaction_uuid}', response_model=Transaction)
    def read_transaction(transaction_uuid: str, transactions_update: TransactionUpdate, db: Session = Depends(get_db)):
        transaction_repository = SQLTransactionRepository(db)
        use_case = UpdateTransactionUseCase(transaction_repository)
        try:
            use_case.execute(transaction_uuid, commission=transactions_update.commission, description=transactions_update.description, transaction_date=transactions_update.date ,related_transaction_id=transactions_update.related_transaction_id)
            updated_transaction = transaction_repository.get(transaction_uuid)
            logging.info(f"transaction update ok: {updated_transaction}")
            return updated_transaction
        except ValueError as e:
            logging.error(f"could not update transaction: {str(e)}")
            raise HTTPException(status_code=404, detail=str(e))
