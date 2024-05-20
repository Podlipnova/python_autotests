import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '934f28339f223a5998ecc87dfc0315c9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID= '4087'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer id': TRAINER_ID})
    assert response.status_code == 200