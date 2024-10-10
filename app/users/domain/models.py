
class User:
    def __init__(self, user_id: int, email: str, full_name: str, phone_number: str, password: str, user_rol: int, profile_picture: str, current_points: int, balance: float):
        self.user_id = user_id
        self.email = email
        self.full_name = full_name
        self.phone_number = phone_number
        self.password = password
        self.user_rol = user_rol
        self.profile_picture = profile_picture
        self.current_points = current_points
        self.balance = balance

    def update_info(self, full_name: str = None, phone_number: str = None):
        if full_name:
            self.full_name = full_name
        if phone_number:
            self.phone_number = phone_number

    @staticmethod
    def create_new_user(email: str, password: str, full_name: str, phone_number: str, user_rol: int, profile_picture: str, current_points: int, balance: float):
        # Aquí puedes agregar más validaciones de negocio si es necesario
        return User(user_id=None, email=email, password=password, full_name=full_name, phone_number=phone_number, user_rol=user_rol, profile_picture=profile_picture, current_points=current_points, balance=balance)
