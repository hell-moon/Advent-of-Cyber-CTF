import requests
import json


path = ''
host = 'http://10.10.112.87:3000/'
value = ''
# path_str = ''
value_str = ''

while(path != 'end' and value != 'end'):
    response = requests.get(host + path)

    # print('\'{}\''.format(response))
    # status_code = response.status_code
    # text = response.text 
    # print(type(text))

    json_response = response.json()
    path = json_response['next']
    value = json_response['value']
    # path_str += path
    if(value != 'end'):
        value_str += value


# print('path_str: {}'.format(path_str))
print('value_str: {}'.format(value_str))

