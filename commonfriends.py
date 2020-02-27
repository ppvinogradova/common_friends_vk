from urllib.parse import urlencode
import requests

APP_ID = 7336572
AUTH_URL = 'https://oauth.vk.com/authorize'
params = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': 5.103
}

#print('?'.join((AUTH_URL, urlencode(params))))

TOKEN = '0dd4e40251dc57543b38a1da1868d1143ce9281cdd2c12e4ff909a7a4b70d1746b18a37d5c08ef24b9319'

class User:

    def __init__ (self, id):
        self.id = id
    
    def __str__(self):
        return f'https://vk.com/id{self.id}'

    def __and__(self, other):
        request_params = {
            'access_token': TOKEN,
            'source_uid': self.id,
            'target_uid': other.id,
            'v': 5.103
        }
        response = requests.get( 
            'https://api.vk.com/method/friends.getMutual',
            params=request_params
        )
        full = response.text
        half = full.split('[')
        c = half[1].split(']')
        ids = c[0].split(',')
        for id_num in ids:
            self.__init__(id_num)
            print(self)
        

user1 = User(261103241)
#print(user1)
user2 = User(244714203)
user1 & user2
    