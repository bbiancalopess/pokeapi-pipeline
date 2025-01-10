# Crie um novo DataFrame que contenha a contagem de Pokémon por tipo.
# Gere um gráfico de barras com matplotlib ou seaborn mostrando a distribuição de Pokémon por tipo.
import matplotlib.pyplot as plt
import seaborn as sea

def generate_type_count_bar_graph(df):
    type_counts = df.explode("Tipos")["Tipos"].value_counts()
    plt.figure(figsize=(12, 6))
    sea.barplot(x=type_counts.index, y=type_counts.values)
    plt.title("Contagem de Pokémon por Tipo")
    plt.xlabel("Tipo")
    plt.ylabel("Contagem")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

def calculate_stats_mean_per_type(df):
    return df.explode("Tipos").groupby("Tipos")[["Ataque", "Defesa", "HP"]].mean().reset_index()

def generate_mean_per_type_grouped_bars_graph(df):
    df_long = df.melt(id_vars="Tipos", var_name="Atributo", value_name="Valor")

    plt.figure(figsize=(12, 6))
    sea.barplot(data=df_long,x="Tipos", y="Valor", hue="Atributo")
    plt.title("Atributos Médios por Tipo")
    plt.xlabel("Valor médio")
    plt.ylabel("Tipos")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

def get_n_best_pokemon_by_experience(df, top_n):
    return df.nlargest(top_n, "Experiência")

def generate_best_pokemon_by_experience_graph(df):
    df_filtered = df[["Nome", "Experiência"]]
    print(df_filtered)
    sea.barplot(data=df_filtered, x="Experiência", y="Nome", orient="h")
    plt.title("Melhores pokémons por Experiência Base")
    plt.xlabel("Experiência")
    plt.ylabel("Pokémon")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt    