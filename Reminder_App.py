from plyer import notification
import time
def reminder():
    notification.notify(title = "take break_from work reminder", 
        message="hello sir please take some break from work",
        timeout = 10)

reminder()
time.sleep(3600)
