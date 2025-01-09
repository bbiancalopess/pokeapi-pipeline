import requests
import logging

def fetch_pokemon_list(limit=100, offset=0):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        raise Exception(f"API error: {response.status_code}")

# refatorar para buscar apenas as informações que preciso, /pokemon/{id} faz uma chamada de api para cada informação do pokemon, exemplo, para moves ele faz /move/1/
def fetch_pokemon_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API error: {response.status_code}")