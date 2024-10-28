from app.notifications.domain.adapters.verification_adapter import VerificationAdapter

class SendVerificationUseCase:
    def __init__(self, verification_adapter: VerificationAdapter):
        self.verification_adapter = verification_adapter

    def execute(self, phone_number: str, verification_code: str):
        mensaje_data = {
            "phone_number": phone_number,
            "verification_code": verification_code
        }
        self.verification_adapter.send_verification_code(mensaje_data)