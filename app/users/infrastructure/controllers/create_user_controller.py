from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.users.infrastructure.repositories.sql_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.create_user_use_case import CreateUserUseCase
from app.users.infrastructure.schemas import UserCreate, User
from app.db import get_db

class CreateUserController:
    def __init__(self) -> None:
        self.use_case = CreateUserUseCase()
        pass

    router = APIRouter()

    @router.post('/users', response_model=User)
    def create_user(self, user_create: UserCreate, db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        self.use_case(user_repository)
        try:
            new_user = self.use_case.execute(
                email=user_create.email,
                password=user_create.password,
                full_name=user_create.full_name,
                phone_number=user_create.phone_number,
                user_rol=user_create.user_rol,
                profile_picture=user_create.profile_picture,
                current_points=user_create.current_points,
                balance=user_create.balance
            )
            return new_user
        except IntegrityError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail="Invalid user role or other integrity constraint violation")
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))