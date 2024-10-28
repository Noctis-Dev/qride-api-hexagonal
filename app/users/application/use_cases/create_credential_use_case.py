from app.users.domain.repositories.credential_repository import CredentialRepository
from app.users.domain.models.credential_model import Credential

class CreateCredentialUseCase:
    def __init__(self, credential_repository: CredentialRepository):
        self.credential_repository = credential_repository

    def execute(self, credential: Credential):
        return self.credential_repository.save(credential)