from app.users.domain.repositories import UserRepository

class DeleteUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_uuid: str):
        user = self.user_repository.get(user_uuid)
        if not user:
            raise ValueError(f"User with uuid {user_uuid} not found")
        self.user_repository.delete(user)
        