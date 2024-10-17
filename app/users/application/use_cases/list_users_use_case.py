from app.users.domain.repositories import UserRepository

class ListUsersUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, skip: int = 0, limit: int = 100):
        return self.user_repository.get_users(skip, limit)