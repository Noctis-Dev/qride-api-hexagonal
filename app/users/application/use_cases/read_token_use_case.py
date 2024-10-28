from app.users.domain.repositories.token_repository import TokenRepository

class ReadTokenUseCase:
    def __init__(self, token_repository: TokenRepository):
        self.token_repository = token_repository
    
    def execute(self, token_uuid: str):
        return self.token_repository.get(token_uuid)