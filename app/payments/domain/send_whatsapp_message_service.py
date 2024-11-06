from abc import ABC, abstractmethod

class WhatsAppClientInterface(ABC):
    @abstractmethod
    async def send_whatsapp_message(self, to: str, template_name: str, language_code: str = "es_MX") -> dict:
        pass