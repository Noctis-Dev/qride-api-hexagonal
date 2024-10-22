from app.payments.domain.transaction_repository import TransactionRepository


class ReadTransactionUseCase:
    def __init__(self, transaction_repository: TransactionRepository) -> None:
        self.transaction_repository = transaction_repository
        pass

    def execute(self, transaction_uuid: str):
        return self.transaction_repository.get(transaction_uuid)
