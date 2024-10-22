from app.payments.domain.transaction_repository import TransactionRepository


class DeleteTransactionUseCase:
    def __init__(self, transaction_repository: TransactionRepository) -> None:
        self.transaction_repository = transaction_repository
        pass

    def execute(self, transaction_uuid: str):
        transaction = self.transaction_repository.get(transaction_uuid)
        if transaction:
            self.transaction_repository.delete(transaction)
            return True
        return False
