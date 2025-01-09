import pandas as pd

def structure_pokemon_data(pokemons):
    data = []
    for pokemon in pokemons:
        types = [type["type"]["name"] for type in pokemon["types"]]
        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in pokemon["stats"]}
        category = "Fraco" if pokemon["base_experience"] < 50 else  "Forte" if pokemon["base_experience"] > 100 else "Médio"
        data.append({
            "ID": pokemon["id"],
            "Nome": pokemon["name"],
            "Experiência": pokemon["base_experience"],
            "Tipos": types,
            "HP": stats.get("hp"),
            "Ataque": stats.get("attack"),
            "Defesa": stats.get("defense"),
            "Categoria": category
        })
    return pd.DataFrame(data)