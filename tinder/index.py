import urllib.request
import json

from sense_hat import SenseHat
s = SenseHat()

def show_info(*infos):
    for info in infos:
        print('displaying: ' + info)
        s.show_message(info)

def get_user():
    with urllib.request.urlopen('https://randomuser.me/api/?=1') as rand_user_api:
        users = json.loads(rand_user_api.read().decode())
        return users['results'][0]

def get_info(user):
    name = user['name']['first'] + ' ' + user['name']['last']
    gender = user['gender']
    city = user['location']['city']
    show_info(name, gender, city)

get_info(get_user())
