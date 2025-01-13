import os
import logging

# Função para salvar um gráfico
def save_plot(plot, filename):
    try:
        os.makedirs("data/", exist_ok=True)
        plot.savefig(filename)
        logging.info(f"Gráfico salvo com sucesso em {filename}")
    except Exception as err:
        logging.error(f"Erro ao salvar gráfico: {err}")

# Função para salvar os relatórios em formato CSV
def save_report(df_mean_by_type, df_best_pokemons):
    try:
        os.makedirs("data/", exist_ok=True)
        df_mean_by_type.to_csv("data/mean_by_type.csv", index=False)
        df_best_pokemons.to_csv("data/best_pokemons_by_experiencia.csv", index=False)
        logging.info("Relatório salvo com sucesso em data/")
    except Exception as err:
        logging.error(f"Erro ao salvar relatório: {err}")