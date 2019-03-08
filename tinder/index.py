# import json
# with open('data.json', 'r') as data:
#     json_data = json.load(data)

# # for user in json_data:
#     # print(json_data['results'])
#     # print(json_data['results'])

# print(json_data['results'][0]['gender'])

import urllib.request
import json
with urllib.request.urlopen('https://randomuser.me/api/') as rand_user_api:
    users = json.loads(rand_user_api.read().decode())
    print(users)
