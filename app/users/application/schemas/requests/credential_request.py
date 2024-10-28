from pydantic import BaseModel

class CredentialRequest(BaseModel):
    contact_uuid: str
    password: str