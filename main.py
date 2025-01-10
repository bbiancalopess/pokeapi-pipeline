from scripts.extract import fetch_pokemon_list, fetch_pokemon_details
from scripts.transform import structure_pokemon_data
from scripts.analyze import generate_type_count_bar_graph, calculate_stats_mean_per_type, get_n_best_pokemon_by_experience, generate_mean_per_type_grouped_bars_graph, generate_best_pokemon_by_experience_graph
from scripts.export import save_plot
import pandas as pd

def main():
    pokemons = fetch_pokemon_list(limit=100, offset=0)
    pokemons_datas = [fetch_pokemon_details(pokemon["url"]) for pokemon in pokemons]
    df = structure_pokemon_data(pokemons_datas)
    
    type_count_plot = generate_type_count_bar_graph(df)
    save_plot(type_count_plot, "type_count.png")
    
    best_pokemon_by_experience = get_n_best_pokemon_by_experience(df, 5)
    best_pokemon_by_experience_plot = generate_best_pokemon_by_experience_graph(best_pokemon_by_experience)
    save_plot(best_pokemon_by_experience_plot, "best_pokemon_by_experience.png")
    
    mean_per_type = calculate_stats_mean_per_type(df)
    mean_per_type_plot = generate_mean_per_type_grouped_bars_graph(mean_per_type)
    save_plot(mean_per_type_plot, "mean_per_type.png")

if __name__ == "__main__":
    main()