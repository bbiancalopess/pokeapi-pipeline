from scripts.extract import fetch_pokemon_list, fetch_pokemon_details
from scripts.transform import structure_pokemon_data
from scripts.analyze import generate_type_count
from scripts.export import save_plot

def main():
    pokemons = fetch_pokemon_list(limit=100, offset=0)
    pokemons_datas = [fetch_pokemon_details(pokemon["url"]) for pokemon in pokemons]
    df = structure_pokemon_data(pokemons_datas)
    type_counts, plot = generate_type_count(df)
    save_plot(plot, "type_count.png")

if __name__ == "__main__":
    main()