from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.users.infrastructure.repositories.sql_user_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.list_users_use_case import ListUsersUseCase
from app.users.infrastructure.schemas import User
from app.db import get_db
import logging
import os

log_dir = "var/log"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, 'myapp.log'), 
    level=logging.INFO,                             
    format='%(asctime)s - %(levelname)s - %(message)s'  
)

class ListUsersController:
    router = APIRouter()

    @router.get('/users', response_model=list[User])
    def list_users(db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        use_case = ListUsersUseCase(user_repository)
        users = use_case.execute(skip= 0, limit= 100)
        logging.info(f"{len(users)} users have been listed.")
        return users