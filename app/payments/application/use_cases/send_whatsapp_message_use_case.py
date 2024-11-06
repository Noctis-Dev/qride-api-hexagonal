from app.payments.domain.send_whatsapp_message_service import WhatsAppClientInterface

class SendWhatsAppMessageUseCase:
    def __init__(self, whatsapp_client: WhatsAppClientInterface):
        self.whatsapp_client = whatsapp_client

    async def execute(self, to: str, template_name: str, language_code: str = "es_MX") -> dict:
        return await self.whatsapp_client.send_whatsapp_message(to, template_name, language_code)