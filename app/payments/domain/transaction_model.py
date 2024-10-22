class Transaction:

    def __init__(self, transaction_id, transaction_uuid, user_id, transaction_type, amount, commission, description, transaction_date, related_transaction_id):
        self.transaction_id = transaction_id
        self.transaction_uuid = transaction_uuid
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.commission = commission
        self.description = description
        self.transaction_date = transaction_date
        self.related_transaction_id = related_transaction_id

    @staticmethod
    def create_new_transaction(user_id, transaction_type, amount, commission, description,
                               transaction_date, related_transaction_id):
        return Transaction(transaction_id=None, transaction_uuid=None, user_id=user_id,
                           transaction_type=transaction_type, amount=amount, commission=commission,
                           description=description, transaction_date=transaction_date,
                           related_transaction_id=related_transaction_id)

    def update_transaction(self, commission=None, description=None,
                           transaction_date=None, related_transaction_id=None):
        if commission:
            self.commission = commission
        if description:
            self.description = description
        if transaction_date:
            self.transaction_date = transaction_date
        if related_transaction_id:
            self.related_transaction_id = related_transaction_id
