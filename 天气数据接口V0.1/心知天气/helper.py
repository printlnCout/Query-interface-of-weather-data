import sys
from .const_value import LOCATION


def getLocation():
    """get location from user input
    default beijing
    """
    location=input("please input the location you want to look at : ")
    if not location:
        location = LOCATION
    return location
