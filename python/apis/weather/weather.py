import os
<<<<<<< HEAD

=======
>>>>>>> master
from pyowm import OWM
from pyowm.utils import config, timestamps

api = os.environ["weatherApi"]
owm = OWM(api)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Sarishabari')
W = observation.weather


def current_weather():
    return(f"{W.detailed_status}")


def current_humidity():
    return(f"current humidity {W.humidity}%")


def current_temperature():
    return f"{W.temperature('celsius')['temp']} degree celsius"


def chance_of_rain():
    if W.rain == {}:
        return("There is no chance of rain now")
    else:
        return("It my rain today")

def cloud_cover():
    return f"cloud cover {W.clouds}%"

