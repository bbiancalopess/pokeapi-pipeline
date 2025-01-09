# Crie um novo DataFrame que contenha a contagem de Pokémon por tipo.
# Gere um gráfico de barras com matplotlib ou seaborn mostrando a distribuição de Pokémon por tipo.
import matplotlib.pyplot as plt
import seaborn as sea

def generate_type_count(df):
    type_counts = df.explode("Tipos")["Tipos"].value_counts()
    plt.figure(figsize=(10, 6))
    sea.barplot(x=type_counts.index, y=type_counts.values)
    plt.title("Contagem de Pokémon por Tipo")
    plt.xlabel("Tipo")
    plt.ylabel("Contagem")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return type_counts, plt