"""Query interface of weather data
   from web : http://www.avatardata.cn/
   finish_time : 2017/9/30
"""
import requests

__version__ = '0.1'
__author__ = 'Lei Chang'
__key__ = '34d7148c58284e9e8940a56488d5a769'


def show_msg(json):
    # Parse the returned jason object and output the parsing results

    # Show the time now
    date = json['result']['realtime']
    print('Place : {0}  Now Time ： {1}  Lunar calendar ： {2} {3}'.
          format(date['city_name'], date['date'], date['moon'], date['time']))

    # Forecast weather conditions
    weather = json['result']['weather']
    we_info = weather[0]['info']
    for k, v in we_info.items():
        print(k, ':', v)
    print()

    # Show life advice
    info = json['result']['life']['info']
    f = {'ziwaixian': 'ultraviolet', 'kongtiao': 'conditioning', 'wuran': 'pollution',
         'ganmao': 'cold', 'xiche': 'car_wash', 'yundong': 'movement',
         'chuanyi': 'dressing'}
    for k, v in info.items():
        print(f[k], ':', v)


url = 'http://api.avatardata.cn/Weather/Query'
city = input('please input the space name you want to ask for：')
value = {
    'key': __key__,
    'cityName': city,
}

"""Use url and value to set the parameter of the request
 And then sent it to get the reply
 Use json() function to translate the result into json form
 Use show_msg　function to output the reply
"""
s = requests.get(url, params=value)
js = s.json()
show_msg(js)
