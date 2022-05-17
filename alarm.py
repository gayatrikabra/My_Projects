import datetime
from playsound import playsound
import datetime
import time
from playsound import playsound
def sound():
    for i in range(2): # Number of repeats
        for j in range(9): # Number of beeps
            playsound("beep.mp3")
            time.sleep(2) # How long between beeps

def alarm():
    x = datetime.datetime.now()
    time_obj = x.strftime("%H:%M")
    alarm_time = input("Enter time to ring alarm!! in format : hr:min")
    if(time_obj == alarm_time):
        try:
            sound()
        except:
            print("Error occured!!")
            
alarm()
            

