import datetime
import os
import subprocess
import sys
from time import sleep

from pywhatkit import playonyt

sys.path.insert(1, os.path.abspath('.'))
from python.song.youtubeData import length


def stop():
  try:
    cmd = subprocess.run(["taskkill", "/im", "chrome.exe"], capture_output=True).stdout.decode()
    cmd = cmd.split(" ")
    cmd = cmd[0].replace(":","")
    if cmd == "SUCCESS":
      return "Stoped"
    else:
      return "Aready Stopted"
  except KeyboardInterrupt:
    exit()


def play(name):
  try:
    return playonyt(name)
  except:
    exit()


def player(name):
    url = play(name)
    leng = length(url)
    hr_min_sec = str(datetime.timedelta(seconds=leng))
    hr_min_sec_split = str(datetime.timedelta(seconds=leng)).split(":")
    min_sec = f"{hr_min_sec_split[1]}:{hr_min_sec_split[2]}"
    hour = int(hr_min_sec_split[0])
    minute = int(hr_min_sec_split[1])
    second = int(hr_min_sec_split[2])

    sleep(1)
    sec = 0
    mun = 0
    hr = 0

    while True:
        try:
            if hour > 0:
              print("{:02d}:{:02d}:{:02d} / {}".format(hr,mun,sec,hr_min_sec), end='\r')
            elif minute > 0:
              print("{:02d}:{:02d} / {}".format(mun,sec,min_sec), end="\r")
            else:
              print("{:02d} / {}".format(sec, second), end="\r")
            sleep(1)
            if sec ==59:
                sec = 0
                sec = sec-1
                mun += 1
            if mun == 59:
                mun = 0
                mun = mun-1
                hr += 1

            if second > 0 or minute > 0 or hour > 0:
                if minute > 0 or hour > 0:
                    if hour > 0:
                        if hr == hour and mun == minute and sec == second:
                          break
                    elif mun == minute and sec == second:
                        break    
                elif sec == second:
                    break
            sec+=1
        except KeyboardInterrupt:
            exit()
    stop()
