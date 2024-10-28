import datetime
import uuid
from sqlalchemy.orm import Session
from app.notifications.domain.repositories.notification_repository import NotificationRepository
from app.notifications.domain.models.notification_model import Notification
from app.notifications.infrastructure.entities.sql_notification_entity import SQLNotification


class SQLNotificationRepository(NotificationRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, notification: Notification) -> None:
        notification_entity = SQLNotification(
            uuid= uuid.uuid4(),
            user_id=notification.user_id,
            title=notification.title,
            message=notification.message,
            created_at=notification.created_at | datetime.datetime.now(),
            notification_type=notification.notification_type
        )
        self.db.add(notification_entity)
        self.db.commit()
        self.db.refresh(notification_entity)
        return None
