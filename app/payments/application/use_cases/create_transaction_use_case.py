from app.payments.domain.transaction_repository import TransactionRepository
from app.payments.domain.transaction_model import Transaction


class CreateTransactionUseCase:
    def __init__(self, transaction_repository: TransactionRepository) -> None:
        self.transaction_repository = transaction_repository
        pass

    def execute(self, user_id: int, transaction_type: str, amount: float, commission: float, description: str, transaction_date: str, related_transaction_id: int):
        new_transaction = Transaction.create_new_transaction(user_id=user_id, transaction_type=transaction_type, amount=amount,
                                                             commission=commission, description=description, transaction_date=transaction_date, related_transaction_id=related_transaction_id)
        return self.transaction_repository.save(new_transaction)
