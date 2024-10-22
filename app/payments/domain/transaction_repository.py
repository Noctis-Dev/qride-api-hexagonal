from abc import ABC, abstractmethod
from typing import Optional
from app.payments.domain.transaction_model import Transaction


class TransactionRepository:
    @abstractmethod
    def get(self, transaction_uuid: str) -> Optional[Transaction]:
        pass

    @abstractmethod
    def get_transactions_by_user(self, skip: int = 0, limit: int = 100, user_id: int = None):
        pass

    @abstractmethod
    def save(self, transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    def update(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def delete(self, transaction: Transaction) -> None:
        pass
