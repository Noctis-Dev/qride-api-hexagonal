from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.users.infrastructure.repositories.sql_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.list_users_use_case import ListUsersUseCase
from app.users.infrastructure.schemas import User
from app.db import get_db

class ListUsersController:
    def __init__(self) -> None:
        self.use_case = ListUsersUseCase()
        pass

    router = APIRouter()

    @router.get('/users', response_model=list[User])
    def list_users(self, db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        self.use_case(user_repository)
        return self.use_case.execute()