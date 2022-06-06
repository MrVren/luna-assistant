#Вывод уведомлений Windows 10. На других ОС необходимо проверить
from plyer import notification


def show_notify(title, message):
    notification.notify(title = title,
                        message = message,
                        timeout = 5)