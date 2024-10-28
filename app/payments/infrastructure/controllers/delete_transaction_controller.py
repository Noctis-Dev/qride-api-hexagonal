from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.payments.infrastructure.repositories.sql_repository import SQLTransactionRepository
from app.payments.application.use_cases.delete_transaction_use_case import DeleteTransactionUseCase
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


class DeleteTransactionController:
    
    router = APIRouter

    @router.delete('/transactions/{transaction_uuid}', response_model=Transaction)
    def delete_transaction(transaction_uuid: int, db: Session = Depends(get_db)):
        transaction_repository = SQLTransactionRepository(db)
        use_case = DeleteTransactionUseCase(transaction_repository)
        
        try:
            
            transaction_to_delete = transaction_repository.get(transaction_uuid)
            if not transaction_to_delete:
                raise HTTPException(status_code=404, detail="Transaction not found")
            
            use_case.execute(transaction_id=transaction_uuid)
            logging.info(f"transaction delete: {transaction_to_delete}")
            return transaction_to_delete 
        except IntegrityError as e:
            db.rollback()
            logging.error(f"Could not create transaction due to integrity constraints: {str(e)}")
            raise HTTPException(status_code=400, detail="Could not delete the transaction due to integrity constraints")
        except ValueError as e:
            logging.error(f"could not delete transaction: {str(e)}")
            raise HTTPException(status_code=400, detail=str(e))