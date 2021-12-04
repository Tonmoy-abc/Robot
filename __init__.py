from time import sleep

from python.apis.arduino.smoke import smoked
from python.apis.configs.conditions import *
from python.apis.configs.functions import *
from python.modules.speech_recognition.speech import Recognize

#Speak("Hellow I am Agraadut your personal assistant")
while True:
    if smoke == False:
        text = Recognize()
        if text != None:
            print(text)
            if text == what_is_your_name or text == who_are_you:
                name(name="Tonmoy", cond="what")
            elif text == who_are_you:
                name(name="Tonmoy", cond="who")
            elif text == what_is_your_fathers_name or text == who_is_your_father:
                fatherNmae()
            elif text == what_is_your_mothers_name or text == who_is_your_mother:
                motherName()
            elif text == what_is_the_name_of_your_country or text == what_is_your_country:
                country()
            elif text == how_old_are_you:
                age(bday=30,bmoth=11,byear=2021)
            elif text == what_is_the_time_by_your_watch or text == what_is_the_time_in_your_watch or text == what_is_the_time or text == show_me_the_time or text == time_now or text == current_time or text == what_is_the_current_time:
                ctime()
        else:
            print(end='\r')
    else:
        continue
