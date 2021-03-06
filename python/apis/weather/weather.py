import os
from pyowm import OWM
from pyowm.utils import config, timestamps

api = os.environ["weatherApi"]
owm = OWM(api)
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Sarishabari')
W = observation.weather


def current_weather():
    return(f"{W.detailed_status}")


# print(w.wind())
def current_humidity():
    return(f"current humidity {W.humidity}%")


def current_temperature():
    return f"current temperature is {W.temperature('celsius')['temp']} degree celsius"


def chance_of_rain():
    return(W.rain)


def cloud_cover():
    return f"cloud cover {W.clouds}%"
# print(w.heat_index)
# print(w.clouds)

#forecast = mgr.forecast_at_place('', 'daily')
# (forecast)
