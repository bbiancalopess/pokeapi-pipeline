from scripts.extract import fetch_pokemon_list, fetch_all_pokemon_details
from scripts.transform import structure_pokemon_data
from scripts.analyze import generate_type_count_bar_graph, calculate_stats_mean_per_type, get_n_best_pokemon_by_experience, generate_top_pokemon_interactive_bar
from scripts.export import save_plot, save_report, save_interactive_plot
import logging

# Função principal
def main():
    try:
        logging.info("Iniciando pipeline...")
        # Busca lista de pokemóns
        logging.info("Buscando lista dde pokemons...")
        pokemons = fetch_pokemon_list(limit=100, offset=0)

        if not pokemons:
            logging.error("Falha ao buscar a lista de pokemons")
            return

        # Busca detalhes dos pokémons
        logging.info("Buscando detalhes dos pokemons...")
        pokemons_datas = fetch_all_pokemon_details(pokemons)
        
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

        interactive_plot = generate_top_pokemon_interactive_bar(df)
        save_interactive_plot(interactive_plot, "data/top_pokemon_interactive.html")

    except Exception as err:
        logging.error(f"Erro inesperado: {err}")

if __name__ == "__main__":
    main()