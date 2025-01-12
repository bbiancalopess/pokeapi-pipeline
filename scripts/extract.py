import requests
import logging
import os

os.makedirs("logs/", exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    filename="logs/pipeline.log", 
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Função para buscar a lista de pokémons com limite e offset
def fetch_pokemon_list(limit=100, offset=0):
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["results"]
        else:
            raise requests.exceptions.HTTPError(f"HTTP error: {response.status_code}")
    except Exception as err:
        logging.error(f"Error: {err}")
    return []

# Função para buscar os detalhes de um pokémon
def fetch_pokemon_details(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise requests.exceptions.HTTPError(f"HTTP error: {response.status_code}")
    except Exception as err:
        logging.error(f"Error: {err}")
    return {}