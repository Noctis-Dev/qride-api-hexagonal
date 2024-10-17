from app.users.domain.repositories import UserRepository
from app.users.domain.models import User

class CreateUserUseCase: 
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository
        pass

    def execute(self, email: str, password: str, full_name: str, phone_number: str, user_rol: int, profile_picture: str, current_points: int, balance: float):
        new_user = User.create_new_user(email=email, password=password, full_name=full_name, phone_number=phone_number, user_rol=user_rol, profile_picture=profile_picture, current_points=current_points, balance=balance)
        return self.user_repository.save(new_user)
