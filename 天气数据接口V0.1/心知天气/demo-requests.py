"""Query interface of weather data
   from web : https://www.seniverse.com/
   finish_time : 2017/9/30
"""
import requests
from const_value import API, KEY, UNIT, LANGUAGE
from helper import getLocation


def fetch_weather(locations):
    """The User API and Key saved in utils.const_value
       getLocation() to get location from user input, default beijing
    """
    result_temp = requests.get(API, params={
        'key': KEY,
        'location': locations,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=1)
    return result_temp.text


if __name__ == '__main__':
    location = getLocation()
    result = fetch_weather(location)
    print(result)
