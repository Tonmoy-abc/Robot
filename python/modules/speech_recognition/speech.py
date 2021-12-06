import time

import pyttsx3

import speech_recognition as sr

r = sr.Recognizer()


def Speak(command, speed='stanard'):
    print("speaking", end="\r", flush="true")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    if speed.lower() == "low":
        engine.setProperty('rate', 110)
    elif speed.lower() == "standard":
        engine.setProperty('rate', 150)
    elif speed.lower() == 'high':
        engine.setProperty('rate', 200)
    else:
        raise ValueError("Un known value {}".format(speed))
    engine.say(command)
    engine.runAndWait()


def PSpeak(command, speed="standard", end="\n"):
    print(command,end=end)
    Speak(command, speed=speed)


def Recognize():
    try:
        with sr.Microphone(device_index=1) as source:
            #r.adjust_for_ambient_noise(source, duration=.2)
            print("listening", end="\r", flush=True)
            audio = r.listen(source, phrase_time_limit=4)
            # Using google to recognize audio
            print("recognizing", end="\r", flush=True)
            print("           ", end="\r")
            MyText = r.recognize_google(audio)
            print("recognized", end='\r', flush=True)
            print("           ", end="\r")
            MyText = MyText.lower()
            return(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
    except KeyboardInterrupt:
        exit()
    except ImportError:
        print("You have to install the requirements\nType the following command=>\npip install -r requirements.txt")


def RawRecognize():
    try:
        with sr.Microphone(device_index=1) as source:
            #r.adjust_for_ambient_noise(source, duration=.2)
            audio = r.listen(source, phrase_time_limit=2)
            # Using google to recognize audio
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
            return(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        pass
    except KeyboardInterrupt:
        exit()
    except ImportError:
        print("You have to install the requirements\nType the following command=>\npip install -r requirements.txt")

