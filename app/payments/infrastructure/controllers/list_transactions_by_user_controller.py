from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.payments.infrastructure.repositories.sql_repository import SQLTransactionRepository
from app.payments.application.use_cases.list_transactions_by_user_user_case import ListTransactionsByUserUseCase
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


class ListTrasnsactionsController:
    
    router = APIRouter

    @router.get('/users/{user_id}/transactions', response_model=List[Transaction])
    def get_user_transactions(user_id: int, db: Session = Depends(get_db)):
        transaction_repository = SQLTransactionRepository(db)
        use_case = ListTransactionsByUserUseCase(transaction_repository)
        
        try:
            
            user_transactions = use_case.execute(skip=0, limit=100, user_id=user_id)
            if not user_transactions:
                raise HTTPException(status_code=404, detail="No transactions found for this user")
            logging.info(f"list ok: {user_transactions}")
            return user_transactions
        except Exception as e:
            logging.error(f"could not get list: {e}")
            raise HTTPException(status_code=500, detail="An error occurred while fetching transactions")