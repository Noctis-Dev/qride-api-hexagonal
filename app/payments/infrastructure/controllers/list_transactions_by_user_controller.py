from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.payments.infrastructure.repositories.sql_repository import SQLTransactionRepository
from app.payments.application.use_cases.list_transactions_by_user_user_case import ListTransactionsByUserUseCase
from app.payments.infrastructure.schemas import TransactionCreate, Transaction
from app.db import get_db


class ListTrasnsactionsController:
    def __init__(self) -> None:
        self.use_case = ListTransactionsByUserUseCase()
        pass
    router = APIRouter

    @router.get('/users/{user_id}/transactions', response_model=List[Transaction])
    def get_user_transactions(self, user_id: int, db: Session = Depends(get_db)):
        transaction_repository = SQLTransactionRepository(db)
        self.use_case(transaction_repository)
        
        try:
            
            user_transactions = self.use_case.execute(skip=0, limit=100, user_id=user_id)
            if not user_transactions:
                raise HTTPException(status_code=404, detail="No transactions found for this user")
            
            return user_transactions
        except Exception as e:
            raise HTTPException(status_code=500, detail="An error occurred while fetching transactions")