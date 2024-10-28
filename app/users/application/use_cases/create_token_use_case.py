from app.users.domain.repositories.token_repository import TokenRepository
from app.users.domain.models.token_model import Token

class CreateTokenUseCase:
    def __init__(self, token_repository: TokenRepository):
        self.token_repository = token_repository
        
    def execute(self, token: Token):
        return self.token_repository.save(token)