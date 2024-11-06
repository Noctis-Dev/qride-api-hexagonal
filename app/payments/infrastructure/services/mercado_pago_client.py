import mercadopago
import os
from dotenv import load_dotenv
from app.payments.domain.mercado_pago_service import MercadoPagoClientInterface

load_dotenv()

class MercadoPagoClient(MercadoPagoClientInterface):
    def __init__(self):
        self.sdk = mercadopago.SDK(os.getenv("ACCESS_TOKEN_MERCADOPAGO"))

    def create_preference(self, preference_data: dict) -> dict:
        preference_response = self.sdk.preference().create(preference_data)
        return preference_response["response"]

    def get_payment(self, payment_id: str) -> dict:
        return self.sdk.payment().get(payment_id)["response"]