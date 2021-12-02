import math
import os
import sys
from datetime import date, datetime

sys.path.insert(1, os.path.abspath('.'))
from python.modules.speech_recognition.speech import PSpeak, Recognize, Speak


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

