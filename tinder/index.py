# import json
# with open('data.json', 'r') as data:
#     json_data = json.load(data)

# # for user in json_data:
#     # print(json_data['results'])
#     # print(json_data['results'])

# print(json_data['results'][0]['gender'])

import urllib.request
import json


def show_info(*infos):
    for info in infos:
        print(info)


with urllib.request.urlopen('https://randomuser.me/api/?=1') as rand_user_api:
    users = json.loads(rand_user_api.read().decode())
    user = users['results'][0]
    gender = user['gender']
    name = user['name']['first'] + ' ' + \
        users['results'][0]['name']['last']
    city = user['location']['city']
    show_info(name, gender, city)
