from app.payments.domain.transaction_repository import TransactionRepository
from app.payments.domain.transaction_model import Transaction


class UpdateTransactionUseCase:
    def __init__(self, transaction_repository: TransactionRepository) -> None:
        self.transaction_repository = transaction_repository
        pass

    def execute(self, transaction_uuid: str = None, commission: float = None, description=None,
                transaction_date=None, related_transaction_id=None):
        transaction = self.transaction_repository.get(transaction_uuid)
        transaction.update_transaction(commission=commission, description=description,
                                       transaction_date=transaction_date, related_transaction_id=related_transaction_id)
        return True
