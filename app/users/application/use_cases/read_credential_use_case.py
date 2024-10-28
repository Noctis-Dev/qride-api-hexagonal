from app.users.domain.repositories.credential_repository import CredentialRepository

class ReadCredentialUseCase:
    def __init__(self, credential_repository: CredentialRepository):
        self.credential_repository = credential_repository
    
    def execute(self, credential_uuid: str):
        return self.credential_repository.get(credential_uuid)