from plyer import notification
import time

notification_title = "GREETINGS FROM Computer!"
notification_message = (
    "Don't Use PC Extensivelu Just drink the water first and have some rest ."
)

while True:
    notification.notify(
        title=notification_title,
        message=notification_message,
        app_icon=None,
        timeout=10,
    )
    time.sleep(10)
