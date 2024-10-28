from enum import Enum

class NotificationType(Enum):
    EMAIL = "email"
    WHATSAPP = "whatsapp"
    APP_NOTIFICATION = "app_notification"