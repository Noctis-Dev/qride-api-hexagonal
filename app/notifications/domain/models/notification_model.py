import datetime
from app.notifications.domain.enums.notification_type import NotificationType


class Notification:
    def __init__(self, id: int, uuid: str, user_id: int, title: str, message: str, created_at: datetime, notification_type: NotificationType):
        self.id = id
        self.uuid = uuid
        self.user_id = user_id
        self.title = title
        self.message = message
        self.created_at = created_at
        self.notification_type = notification_type