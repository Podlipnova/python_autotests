import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '934f28339f223a5998ecc87dfc0315c9'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_sozdanie = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

'''response = requests.post(url = f'{URL}/pokemons', headers=HEADER, json = body_sozdanie)
print(response.text)'''

body_izmenenie = {   
     "pokemon_id": "27453",
    "name": "RUt",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

'''response_izmenenie = requests.put(url = f'{URL}/pokemons',headers=HEADER, json = body_izmenenie)
print(response_izmenenie.text)'''

body_poimat = {
    "pokemon_id": "27453"
}

response_poimat = requests.post (url= f'{URL}/trainers/add_pokeball',headers=HEADER,json =body_poimat)
print(response_poimat)

