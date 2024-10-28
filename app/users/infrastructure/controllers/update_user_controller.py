from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.users.infrastructure.repositories.sql_user_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.update_user_use_case import UpdateUserUseCase
from app.users.infrastructure.schemas import UserUpdate, User
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

class UpdateUserController:
    router = APIRouter()

    @router.put('/users/{user_uuid}', response_model=User)
    def update_user(user_uuid: str, user_update: UserUpdate, db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        use_case = UpdateUserUseCase(user_repository)
        logging.info(f"Trying to update user with UUID: {user_uuid}")
        try:
            use_case.execute(user_uuid, full_name=user_update.full_name, phone_number=user_update.phone_number)
            updated_user = user_repository.get(user_uuid)
            logging.info(f"User with UUID {user_uuid} updated.")
            return updated_user
        except ValueError as e:
            logging.error(f"Error updating user with UUID {user_uuid}: {str(e)}")
            raise HTTPException(status_code=404, detail=str(e))