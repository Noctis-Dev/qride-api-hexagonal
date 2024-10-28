from app.users.domain.repositories.credential_repository import CredentialRepository
from app.users.domain.models.credential_model import Credential
from app.users.domain.models.contact_model import Contact
from app.users.domain.models.token_model import Token
from app.users.application.schemas.requests.credential_request import CredentialRequest
from app.users.application.mappers.credential_mapper import CredentialMapper


class CreateCredentialUseCase:
    def __init__(self, credential_repository: CredentialRepository):
        self.credential_repository = credential_repository

    def execute(self, request: CredentialRequest, contact: Contact, token: Token ):
        credential = CredentialMapper.to_domain(request)
        credential.contact = contact
        credential.token = token
        return self.credential_repository.save(credential)