from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.payments.application.use_cases.create_and_process_subscription_use_case import CreateAndProcessSubscriptionUseCase
from app.payments.infrastructure.services.mercado_pago_client import MercadoPagoClient
from app.payments.infrastructure.schemas import MPPaymentRequest
from app.payments.infrastructure.repositories.sql_repository import SQLTransactionRepository
from app.payments.infrastructure.services.whatsapp_client import WhatsAppClient
from app.db import get_db
import logging
import os

log_dir = "var/log"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, 'miapp.log'), 
    level=logging.INFO,                             
    format='%(asctime)s - %(levelname)s - %(message)s'  
)

class CreateSubscriptionController:
    
    router = APIRouter()

    @router.post("/payments/mercadopago/subscription")
    def create_subscription(payment_request: MPPaymentRequest, db: Session = Depends(get_db)):
        try:
            logging.info("Solicitud de suscripción recibida para user_id: %s", payment_request.user_id)
            transaction_repository = SQLTransactionRepository(db)
            mercado_pago_client = MercadoPagoClient()
            whatsapp_client = WhatsAppClient()
            create_subscription_use_case = CreateAndProcessSubscriptionUseCase(transaction_repository, mercado_pago_client, whatsapp_client)
            response = create_subscription_use_case.execute(payment_request)
            logging.info("Suscripción creada exitosamente para user_id: %s", payment_request.user_id)
            return response
        except Exception as e:
            logging.error("Error al crear la suscripción para user_id: %s, error: %s", payment_request.user_id, str(e))
            raise HTTPException(status_code=500, detail="Error Interno del Servidor")