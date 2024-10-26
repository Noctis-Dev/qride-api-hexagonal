from typing import List, Optional
import uuid
from sqlalchemy.orm import Session
from app.payments.domain.transaction_model import Transaction
from app.payments.domain.transaction_repository import TransactionRepository
from app.payments.infrastructure.models.sql_transaction_model import Transaction as TransactionModel


class SQLTransactionRepository(TransactionRepository):
    def __init__(self, db: Session):
        self.db = db

    def get(self, transaction_uuid: str) -> Optional[Transaction]:
        transaction_model = self.db.query(TransactionModel).filter(
            TransactionModel.transaction_uuid == transaction_uuid).first()
        if transaction_model:
            return Transaction(
                transaction_id=transaction_model.transaction_id,
                transaction_uuid=transaction_model.transaction_uuid,
                user_id=transaction_model.user_id,
                transaction_type=transaction_model.transaction_type,
                amount=transaction_model.amount,
                commission=transaction_model.commission,
                description=transaction_model.description,
                transaction_date=transaction_model.transaction_date,
                related_transaction_id=transaction_model.related_transaction_id
            )
        return None

    def get_transactions_by_user(self, skip: int = 0, limit: int = 100, user_id: int = None) -> Optional[List[Transaction]]:
        transaction_models = self.db.query(TransactionModel).filter(
            TransactionModel.user_id == user_id).offset(skip).limit(limit).all()
        if transaction_models:
            return [
                Transaction(
                    transaction_id=transaction_model.transaction_id,
                    transaction_uuid=transaction_model.transaction_uuid,
                    user_id=transaction_model.user_id,
                    transaction_type=transaction_model.transaction_type,
                    amount=transaction_model.amount,
                    commission=transaction_model.commission,
                    description=transaction_model.description,
                    transaction_date=transaction_model.transaction_date,
                    related_transaction_id=transaction_model.related_transaction_id
                )
                for transaction_model in transaction_models
            ]
        return None

    def save(self, transaction: Transaction) -> Optional[Transaction]:
        user_model = TransactionModel(
            transaction_uuid=uuid.uuid4(),
            user_id=transaction.user_id,
            transaction_type=transaction.transaction_type,
            amount=transaction.amount,
            commission=transaction.commission,
            description=transaction.description,
            transaction_date=transaction.transaction_date,
            related_transaction_id=transaction.related_transaction_id
        )
        self.db.add(user_model)
        self.db.commit()
        self.db.refresh(user_model)
        return Transaction(
            transaction_id=user_model.transaction_id,
            transaction_uuid=user_model.transaction_uuid,
            user_id=user_model.user_id,
            transaction_type=user_model.transaction_type,
            amount=user_model.amount,
            commission=user_model.commission,
            description=user_model.description,
            transaction_date=user_model.transaction_date,
            related_transaction_id=user_model.related_transaction_id
        )

    def update(self, transaction: Transaction) -> None:
        transaction_model = self.db.query(TransactionModel).filter_by(
            transaction_id=transaction.transaction_id).first()
        if transaction_model:
            transaction_model.commission = transaction.commission
            transaction_model.description = transaction.description
            transaction_model.transaction_date = transaction.transaction_date
            transaction_model.related_transaction_id = transaction.related_transaction_id
            self.db.commit()
            self.db.refresh(transaction_model)
        else:
            raise ValueError(f"Transaction with id {transaction.transaction_id} not found")

    def delete(self, transaction: Transaction) -> None:
        transaction_model = self.db.query(TransactionModel).filter_by(
            transaction_id=transaction.transaction_id).first()
        if transaction_model:
            self.db.delete(transaction_model)
            self.db.commit()
        else:
            raise ValueError(f"Transaction with id {transaction.transaction_id} not found")
