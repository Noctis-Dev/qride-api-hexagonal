from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.users.infrastructure.repositories.sql_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.read_user_by_email_use_case import ReadUserByEmailUseCase
from app.users.infrastructure.schemas import User
from app.db import get_db

class ReadUserByEmailController:
    def __init__(self) -> None:
        self.use_case = ReadUserByEmailUseCase()
        pass

    router = APIRouter()

    @router.get('/users/{email}', response_model=User)
    def read_user_by_email(self, email: str, db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        self.use_case(user_repository)
        try:
            user = self.use_case.execute(email)
            return user
        except ValueError as e:
            raise HTTPException(status_code=404, detail=str(e))