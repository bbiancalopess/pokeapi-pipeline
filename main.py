from scripts.extract import fetch_pokemon_list, fetch_pokemon_details
from scripts.transform import structure_pokemon_data
from scripts.analyze import generate_type_count_bar_graph, calculate_stats_mean_per_type, get_n_best_pokemon_by_experience
from scripts.export import save_plot, save_report
import logging

# Função principal
def main():
    # Busca lista de pokemóns
    logging.info("Buscando lista dde pokemons...")
    pokemons = fetch_pokemon_list(limit=100, offset=0)

    if not pokemons:
        logging.error("Falha ao buscar a lista de pokemons")
        return

    # Busca detalhes dos pokémons
    logging.info("Buscando detalhes dos pokemons...")
    pokemons_datas = [fetch_pokemon_details(pokemon["url"]) for pokemon in pokemons]
    
    # Estrutura os dados dos pokémons
    logging.info("Estruturando dados dos pokemons...")
    df = structure_pokemon_data(pokemons_datas)
    
    # Gera gráfico de contagem de pokémons por tipo
    type_count_plot = generate_type_count_bar_graph(df)
    save_plot(type_count_plot, "data/type_count.png")
    
    # Pega os N melhores pokémons por experiência
    df_best_pokemon_by_experience = get_n_best_pokemon_by_experience(df, 5)
    
    # Calcula a média dos stats por tipo
    df_mean_per_type = calculate_stats_mean_per_type(df)

    # Salva relatórios CSV
    logging.info("Salvando relatorios...")
    save_report(df_mean_per_type, df_best_pokemon_by_experience)

if __name__ == "__main__":
    main()