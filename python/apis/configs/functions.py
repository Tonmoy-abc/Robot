import math
import os
import sys
from datetime import date, datetime

sys.path.insert(1, os.path.abspath('.'))
from python.apis.google_search.search import search_description
from python.apis.weather.weather import (chance_of_rain, cloud_cover,
                                         current_humidity, current_temperature,
                                         current_weather)
from python.modules.speech_recognition.speech import PSpeak, Recognize, Speak
from python.song.song import player


def How_are_you():
    PSpeak("I am fine and you?")
def Hi():
    PSpeak("Hellow ")

def name(name, cond):
    if cond == "what":
      PSpeak(f"My name is {name}")
    elif cond == "who":
      PSpeak(f"I am {name}")

def fatherNmae():
    PSpeak("Sorry, I am not a human so I don't have father.")


def motherName():
    PSpeak("Sorry, I am not a human so I don't have mother")


def country():
    PSpeak("I don't have cityzenship of any country buy currently I am in Bangladesh")


def location():
    pass


def age(bday,bmoth,byear):
    def dateToday():
        today = date.today()
        return today.strftime("%Y,%m,%d")
      
    def strToint(string):
        return int(string)
      
    arr = dateToday().split(',')
    cDate = tuple(map(strToint, arr))
    age = date(cDate[0],cDate[1], cDate[2])-date(byear,bmoth,bday)
    days = int(str(age).split(',')[0].split(" ")[0])
    
    year = 0
    month = 0
    if days > 365:
        year = int(str(days/365).split('.')[0])
        days = days-365
        
    if days > 30:
        month = int(str(days/30).split('.')[0])
        print(month)
        days = days-30
        
    if year >= 1:
        PSpeak(f"I am {year} years old")
    elif month >= 1:
        if month < 6:
            PSpeak("I am less then half years old")
        elif month >= 6:
            PSpeak(f"I am {month} months old")
    elif days > 0:
        PSpeak(f"I am {days} days old")


def ctime():
    current_time = datetime.today().strftime("%I:%M %p")
    PSpeak(f"Now it is {current_time}") 


def liveIn():
    PSpeak("I am currently living in Jamalpur,Bangladesh")


def cTemp(end="\n"):
    PSpeak(f"Now it is {current_temperature()}",end=end)


def cHumi(end='\n'):
    PSpeak(current_humidity(),end=end)


def cloudC(end="\n"):
    PSpeak(cloud_cover(),end=end)


def cRain(end='\n'):
    PSpeak(chance_of_rain(),end=end)


def weatherForcast():
    cTemp()
    cHumi()
    cloudC()
    cRain()        


def What_is_humidity():
    PSpeak("Humidity is the concentration of water vapour present in the air. Water vapor, the gaseous state of water, is generally invisible to the human eye. Humidity indicates the likelihood for precipitation, dew, or fog to be present. Humidity depends on the temperature and pressure of the system of interest")

## PLAY Function

def Play(name):
    print("Playing "+ name, end="\n")
    player(name)
    print("          ", end="\r")

def google_Search(keyword):
    search_description(keyword)
