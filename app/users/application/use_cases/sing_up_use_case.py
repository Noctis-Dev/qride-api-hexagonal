from app.users.application.use_cases.create_token_use_case import CreateTokenUseCase
from app.users.application.use_cases.create_credential_use_case import CreateCredentialUseCase
from app.users.application.use_cases.create_user_use_case import CreateUserUseCase
from app.users.application.use_cases.read_contact_use_case import ReadContactUseCase
from app.users.application.schemas.requests.credential_request import CredentialRequest

class SingUpUseCase: 
    def __init__(self, read_contact_use_case: ReadContactUseCase, create_user_use_case: CreateUserUseCase, create_credential_use_case: CreateCredentialUseCase, create_token_use_case: CreateTokenUseCase):
        self.read_contact_use_case = read_contact_use_case
        self.create_user_use_case = create_user_use_case
        self.create_credential_use_case = create_credential_use_case
        self.create_token_use_case = create_token_use_case
        pass
    
    def execute(self, request: CredentialRequest):
        contact = self.read_contact_use_case.execute(request.contact_uuid)
        token = self.create_token_use_case.execute()
        
        credential = self.create_credential_use_case.execute(request, contact, token)
        
        
        return credential
        