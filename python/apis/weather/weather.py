from pyowm import OWM
from pyowm.utils import config, timestamps

owm = OWM('04e70ef1d8d7c81b88d848c8d285883e')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Sarishabari')
W = observation.weather


def current_weather():
    return(f"{W.detailed_status}")


def current_humidity():
    return(f"current humidity {W.humidity}%")


def current_temperature():
    return f"current temperature is {W.temperature('celsius')['temp']} degree celsius"


def chance_of_rain():
    return(W.rain)


def cloud_cover():
    return f"cloud cover {W.clouds}%"

