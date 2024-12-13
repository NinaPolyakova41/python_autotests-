import requests
URL='https://api.pokemonbattle.ru/v2'
TOKEN='b2d104f1677bcb2441d3703449a696f7'
HEADER= {'Content-Type':'application/json','trainer_token':TOKEN}
body_registration={
    "name": "Пробный 1",
    "photo_id": "12"
}
body_put={
    "pokemon_id": "157974",
    "name": "New Name",
    "photo_id": "2"
}
body_pokeboll={
    "pokemon_id": "157974"
}

'''response = requests.post(url=f'{URL}/pokemons',headers=HEADER,json= body_registration)
print(response.text)'''

'''response = requests.put(url=f'{URL}/pokemons',headers=HEADER,json= body_put)
print(response.text)'''

response = requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json= body_pokeboll)
print(response.text)