from sqlalchemy.orm import Session
from fastapi import Depends
from app.db import get_db
from app.notifications.application.use_cases.send_verification_use_case import SendVerificationUseCase
from app.notifications.application.use_cases.create_notification_use_case import CreateNotificationUseCase
from app.notifications.infrastructure.adapters.whatsapp_verification_adapter import WhatsAppAdapter
from app.notifications.infrastructure.repositories.sql_notification_repository import SQLNotificationRepository
from pyee import EventEmitter

class UserVerificationListener:
    event_emitter = EventEmitter()
    
    @event_emitter.on("user_verification")
    def create_verification_notification(notification_data: dict, db: Session = Depends(get_db)):
        phone_number = notification_data.get("tittle")
        token = notification_data.get("message")
        notification_type = notification_data.get("notification_type")
        if notification_type == "whatsapp":
            verification_adapter = WhatsAppAdapter()
            send_verification_use_case = SendVerificationUseCase(verification_adapter)
            send_verification_use_case.execute(phone_number, token)
        
        notification_repository = SQLNotificationRepository(db)
        create_notification_use_case = CreateNotificationUseCase(notification_repository)
        create_notification_use_case.execute(notification_data)
        pass