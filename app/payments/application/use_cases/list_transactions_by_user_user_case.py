from app.payments.domain.transaction_repository import TransactionRepository


class ListTransactionsByUserUseCase:
    def __init__(self, transaction_repository: TransactionRepository) -> None:
        self.transaction_repository = transaction_repository
        pass

    def execute(self, skip: int = 0, limit: int = 100, user_id: int = None):
        return self.transaction_repository.get_transactions_by_user(skip=skip, limit=limit, user_id=user_id)
