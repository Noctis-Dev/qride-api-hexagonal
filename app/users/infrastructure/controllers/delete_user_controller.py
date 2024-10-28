from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.users.infrastructure.repositories.sql_user_repository import SQLAlchemyUserRepository
from app.users.application.use_cases.delete_user_use_case import DeleteUserUseCase
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

class DeleteUserController:
    
    router = APIRouter()

    @router.delete('/users/{user_uuid}', response_model=User)
    def delete_user(user_uuid: str, db: Session = Depends(get_db)):
        user_repository = SQLAlchemyUserRepository(db)
        use_case = DeleteUserUseCase(user_repository)
        logging.info(f"Trying to delete user with UUID: {user_uuid}")
        try:
            use_case.execute(user_uuid)
            deleted_user = user_repository.get(user_uuid)
            logging.info(f"User with UUID {user_uuid} deleted.")
            return deleted_user
        except ValueError as e:
            logging.error(f"Error deleting user with UUID {user_uuid}: {str(e)}")
            raise HTTPException(status_code=404, detail=str(e))