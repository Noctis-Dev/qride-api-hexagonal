from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.users.application.schemas.requests.contact_request import ContactRequest
from app.users.application.use_cases.create_contact_use_case import CreateContactUseCase
from app.users.infrastructure.repositories.sql_contact_repository import SQLContactRepository
from app.shared.base_response import BaseResponse
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

class CreateContactController:
    router = APIRouter()
    
    @router.post('/contacts', response_model=BaseResponse)
    def create_contact(contact_create: ContactRequest, db: Session = Depends(get_db)):
        contact_repository = SQLContactRepository(db)
        use_case = CreateContactUseCase(contact_repository)
        logging.info(f"Trying to create contact with email: {contact_create.email}")
        try:
            new_contact = use_case.execute(
                contact_create
            )
            logging.info(f"Contact with email {contact_create.email} created successfully.")
            return BaseResponse(message='Se creo el contacto', data=new_contact, success=True, error=None)
        except IntegrityError as e:
            db.rollback()
            logging.error(f"Error creating contact {contact_create.email} due to integrity constraints: {str(e)}")
            error_response = BaseResponse(
                message="Invalid contact data or other integrity constraint violation",
                success=False,
                error=str(e)
            )
            raise HTTPException(status_code=400, detail=error_response.dict())
        except ValueError as e:
            logging.error(f"Error creating contact {contact_create.email}: {str(e)}")
            error_response = BaseResponse(
                message=str(e),
                success=False,
                error=str(e)
            )
            raise HTTPException(status_code=400, detail=error_response.dict())

