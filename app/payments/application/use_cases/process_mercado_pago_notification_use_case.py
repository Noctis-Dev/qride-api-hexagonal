from app.payments.domain.mercado_pago_service import MercadoPagoClientInterface
from app.payments.application.schemas.TransactionUpdate import TransactionUpdate

class ProcessMercadoPagoNotificationUseCase:
    def __init__(self, mercado_pago_client: MercadoPagoClientInterface, transaction_service: TransactionUpdate):
        self.mercado_pago_client = mercado_pago_client
        self.transaction_service = transaction_service

    def execute(self, notification: dict) -> None:
        if notification["type"] == "payment":
            payment_id = notification["data"]["id"]
            payment = self.mercado_pago_client.get_payment(payment_id)

            if payment["status"] == "approved":
                self.transaction_service.update_transaction_by_uuid(payment["external_reference"], {"description": "Payment approved"})
            elif payment["status"] == "rejected":
                self.transaction_service.update_transaction_by_uuid(payment["external_reference"], {"description": "Payment rejected"})