import os

# Função para salvar um gráfico
def save_plot(plot, filename):
    os.makedirs("data/", exist_ok=True)
    plot.savefig(filename)

# Função para salvar os relatórios em formato CSV
def save_report(df_mean_by_type, df_best_pokemons):
    os.makedirs("data/", exist_ok=True)
    df_mean_by_type.to_csv("data/mean_by_type.csv", index=False)
    df_best_pokemons.to_csv("data/best_pokemons_by_experiencia.csv", index=False)