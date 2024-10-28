from app.notifications.domain.repositories.notification_repository import NotificationRepository
from app.notifications.application.mappers.notification_mapper import NotificationMapper
class CreateNotificationUseCase:
    def __init__(self, notification_repository: NotificationRepository):
        self.notification_repository = notification_repository
        pass

    def execute(self, notification: dict) -> None:
        notification_model = NotificationMapper.to_domain(notification)
        self.notification_repository.save(notification_model)
        return None