import requests
import logging

def fetch_pokemon_list(limit=100, offset=0):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        raise Exception(f"API error: {response.status_code}")

def fetch_pokemon_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API error: {response.status_code}")