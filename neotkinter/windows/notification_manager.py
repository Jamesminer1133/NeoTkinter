from .notification_panel import NotificationPanel
from .notification_type import NotifyType as notify_type

class NotificationManager:
    def __init__(self, master):
        self.master = master
        self.notifications = []

    def showNotification(self, message, notify_type=notify_type.INFO, duration=5000, bg_color=None, text_color=None):
        NotificationPanel(self.master, self, message, notify_type=notify_type, duration=duration, bg_color=bg_color, text_color=text_color)

    def addNotification(self, notification):
        self.notifications.append(notification)
        self.updateNotification_positions()

    def removeNotification(self, notification):
        if notification in self.notifications:
            self.notifications.remove(notification)
        self.updateNotification_positions()

    def updateNotification_positions(self):
        for index, notification in enumerate(self.notifications):
            y_offset = -20 - (index * 70)  # Adjust height as necessary
            notification.place(relx=1.0, rely=1.0, x=-20, y=y_offset, anchor="se")