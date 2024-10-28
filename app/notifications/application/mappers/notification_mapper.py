from app.notifications.domain.models.notification_model import Notification
from app.notifications.domain.enums.notification_type import NotificationType

class NotificationMapper:
    @staticmethod
    def to_domain(notification: dict) -> Notification:
        return Notification(
            id=None,
            uuid=None,
            user_id=notification['user_id'],
            title=notification['title'],
            message=notification['message'],
            created_at=notification['created_at'] if 'created_at' in notification else None,
            notification_type= NotificationType(notification['notification_type'].upper())
        )

    @staticmethod
    def to_dict(notification: Notification) -> dict:
        return {
            'id': notification.id,
            'uuid': notification.uuid,
            'user_id': notification.user_id,
            'title': notification.title,
            'message': notification.message,
            'created_at': notification.created_at,
            'notification_type': notification.notification_type
        }