from app.users.application.use_cases.create_token_use_case import CreateTokenUseCase
from app.users.application.use_cases.create_credential_use_case import CreateCredentialUseCase
from app.users.application.use_cases.create_user_use_case import CreateUserUseCase
from app.users.application.use_cases.read_contact_use_case import ReadContactUseCase
from app.users.application.schemas.requests.credential_request import CredentialRequest
from app.users.domain.repositories.token_repository import TokenRepository
from app.users.domain.repositories.credential_repository import CredentialRepository
from app.users.domain.repositories.user_repository import UserRepository
from app.users.domain.repositories.contact_repository import ContactRepository

class SingUpUseCase: 
    def __init__(self, token_repository: TokenRepository, credential_repository: CredentialRepository, 
                 user_repository: UserRepository, contact_repository: ContactRepository):
        self.read_contact_use_case = ReadContactUseCase(contact_repository=contact_repository)
        self.create_user_use_case = CreateUserUseCase(user_repository=user_repository)
        self.create_credential_use_case = CreateCredentialUseCase(credential_repository=credential_repository)
        self.create_token_use_case = CreateTokenUseCase(token_repository=token_repository)
        pass
    
    def execute(self, request: CredentialRequest):
        contact = self.read_contact_use_case.execute(request.contact_uuid)
        token = self.create_token_use_case.execute()
        
        credential = self.create_credential_use_case.execute(request, contact, token)
        
        
        
        return credential
        