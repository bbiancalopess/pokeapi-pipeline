import pandas as pd
import logging

# Função para organizar os dados dos pokémons
def structure_pokemon_data(pokemons):
    data = []
    for pokemon in pokemons:
        if not pokemon: 
            continue

        if not all(key in pokemon for key in ["id", "name", "base_experience", "types", "stats"]):
            logging.error("Erro: dados faltando para pokemons.")
            continue

        types = [type["type"]["name"].capitalize() for type in pokemon["types"]]
        if not types:
            continue

        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in pokemon["stats"]}
        if not all(k in stats for k in ["hp", "attack", "defense"]):
            continue
        
        category = "Fraco" if pokemon["base_experience"] < 50 else  "Forte" if pokemon["base_experience"] > 100 else "Médio"
        data.append({
            "ID": pokemon["id"],
            "Nome": pokemon["name"].capitalize(),
            "Experiência": pokemon["base_experience"],
            "Tipos": types,
            "HP": stats.get("hp"),
            "Ataque": stats.get("attack"),
            "Defesa": stats.get("defense"),
            "Categoria": category
        })
    return pd.DataFrame(data)