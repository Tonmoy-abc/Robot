import os
import sys

from pywhatkit.misc import info

sys.path.insert(1, os.path.abspath('.'))
from python.apis.tanslate.translate import transtate


def information(text):
    if text != "": 
        text = info(text, return_value=True, lines="6")
        text = transtate(text)
        return text
    else:
        return "Give keyword to search"

print(information("Pizza"))
