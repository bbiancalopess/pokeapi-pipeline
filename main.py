from scripts.extract import fetch_pokemon_list, fetch_pokemon_details
from scripts.transform import structure_pokemon_data
from scripts.analyze import generate_type_count_bar_graph, calculate_stats_mean_per_type, get_n_best_pokemon_by_experience
from scripts.export import save_plot, save_report

def main():
    pokemons = fetch_pokemon_list(limit=100, offset=0)
    pokemons_datas = [fetch_pokemon_details(pokemon["url"]) for pokemon in pokemons]
    df = structure_pokemon_data(pokemons_datas)
    
    type_count_plot = generate_type_count_bar_graph(df)
    save_plot(type_count_plot, "data/type_count.png")
    
    df_best_pokemon_by_experience = get_n_best_pokemon_by_experience(df, 5)
    df_mean_per_type = calculate_stats_mean_per_type(df)
    save_report(df_mean_per_type, df_best_pokemon_by_experience)

if __name__ == "__main__":
    main()