from app.payments.application.use_cases.create_transaction_use_case import CreateTransactionUseCase
from app.payments.domain.mercado_pago_service import MercadoPagoClientInterface
from app.payments.domain.transaction_repository import TransactionRepository
from app.payments.application.use_cases.send_whatsapp_message_use_case import SendWhatsAppMessageUseCase
from app.payments.infrastructure.services.whatsapp_client import WhatsAppClient

class CreateAndProcessSubscriptionUseCase:
    def __init__(self, mercado_pago_client: MercadoPagoClientInterface, transaction_repository: TransactionRepository, whatsapp_client: WhatsAppClient) -> None:
        self.create_transaction_repository = CreateTransactionUseCase(transaction_repository)
        self.send_whatsapp_message_use_case = SendWhatsAppMessageUseCase(whatsapp_client)
        self.mercado_pago_client = mercado_pago_client

    def execute(self, transaction):
        preference_data = {
            "items": [{"title": "Subscription", "quantity": 1, "unit_price": transaction.amount}],
            "back_urls": {
                "success": "https://yourapp.com/success",
                "failure": "https://yourapp.com/failure",
                "pending": "https://yourapp.com/pending"
            },
            "external_reference": transaction.id
        }
        preference_response = self.mercado_pago_client.create_preference(preference_data)

        self.send_whatsapp_message_use_case.execute(transaction.user_id, "subscription", "es_MX")

        return preference_response
    
