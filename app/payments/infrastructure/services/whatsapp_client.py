import os
import json
import requests
from dotenv import load_dotenv
from app.payments.domain.send_whatsapp_message_service import WhatsAppClientInterface

load_dotenv()

class WhatsAppClient(WhatsAppClientInterface):
    def __init__(self):
        self.auth_token = os.getenv("WHATSAPP_AUTH_TOKEN")
        self.api_url = "https://graph.facebook.com/v20.0/470243629495943/messages"

    async def send_whatsapp_message(self, to: str, template_name: str, language_code: str = "es_MX") -> dict:
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                }
            }
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth_token}"
        }

        try:
            response = requests.post(self.api_url, headers=headers, data=json.dumps(payload), timeout=30)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return {
                "status": "error",
                "details": str(e)
            }

        if response.status_code == 200:
            return {"status": "success", "message": "Mensaje enviado"}
        else:
            return {
                "status": "error",
                "code": response.status_code,
                "details": response.text
            }