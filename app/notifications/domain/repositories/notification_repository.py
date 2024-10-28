# domain/repositories/notification_repository.py
from abc import ABC, abstractmethod
from app.notifications.domain.models.notification_model import Notification

class NotificationRepository(ABC):
    @abstractmethod
    def save(self, notification: Notification) -> None:
        pass
