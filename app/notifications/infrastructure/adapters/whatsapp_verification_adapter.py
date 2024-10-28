from app.notifications.domain.adapters.verification_adapter import VerificationAdapter

class WhatsAppAdapter(VerificationAdapter):
    def send_verification_code(self, mensaje_data: dict):
        numero = mensaje_data.get("numero")
        mensaje = mensaje_data.get("mensaje")
        
        
