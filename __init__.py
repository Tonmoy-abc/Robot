from time import sleep

from python.apis.arduino.smoke import smoked
from python.apis.configs.conditions import *
from python.apis.configs.functions import *
from python.modules.speech_recognition.speech import PSpeak, Recognize

#Speak("Hellow I am Agraadut your personal assistant")
while True:
    smoke = False
    if smoke == False:
        text = Recognize()
        if text != None:
            print(text)
            if text == hi:
                Hi()
            elif text.split(" ")[0] == hi:
                text = text.replace("hi", "").strip()
                if text == what_is_your_name or text == who_are_you:
                    name(name="Tonmoy", cond="what")
                elif text == how_are_you:
                    How_are_you()
            elif text == how_are_you:
                How_are_you()
            elif text == what_is_your_name:
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
            elif (text == what_is_the_time_by_your_watch or text == what_is_the_time_in_your_watch or text == what_is_the_time or 
                  text == show_me_the_time or text == time_now or text == current_time or text == what_is_the_current_time or text==tell_me_the_time):
                ctime()
            elif text == what_is_the_current_weather or text == tell_me_about_the_weather or text == current_weather or text == weather or text == todays_weather:
                weatherForcast()
            elif text == what_is_the_current_temperature or text == current_temperature or text == temperature or text == temperature_now:
                cTemp()
            elif text == what_is_the_current_humidity or text == current_humidity or text == humidity or text == humidity_now:
                cHumi()
            elif text == what_is_humidity:
                what_is_humidity()
            elif text.split(" ")[0] == play:
                song = text.replace("play", "").strip()
                if song != "":
                    if text == play_amar_sonar_bangla or text == play_the_national_anthem_of_bangladesh or text == play_the_national_song_of_bangladesh:
                        Play("https://www.youtube.com/watch?v=zVjbVPFeo2o")
                    else:
                        Play(song)
                else:
                    PSpeak("What to play? You don't say anything after play")
                print("          ", end="\r")
            elif text.split(" ")[0] == sing:
                song = text.replace("sing", "").strip()
                if song != "":
                    if text == sing_amar_sonar_bangla or text == sing_the_national_anthem_of_bangladesh or text == sing_the_national_song_of_bangladesh:
                        Play("https://www.youtube.com/watch?v=zVjbVPFeo2o")
                    else:
                        Play(song)
                else:
                    PSpeak("What to sing? You don't say anything after sing")
                print("          ", end="\r")
            else:
                continue
        else:
            print(end='\r')
    else:
        continue
