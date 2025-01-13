import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

# Função para gerar o gráfico de contagem por tipo
def generate_type_count_bar_graph(df):
    type_counts = df.explode("Tipos")["Tipos"].value_counts()
    plt.figure(figsize=(12, 6))
    plt.bar(type_counts.index, type_counts.values)
    plt.title("Contagem de Pokémon por Tipo")
    plt.xlabel("Tipo")
    plt.ylabel("Contagem")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

# Função para calcular a média dos stats por tipo
def calculate_stats_mean_per_type(df):
    return df.explode("Tipos").groupby("Tipos")[["Ataque", "Defesa", "HP"]].mean().reset_index()

# Função para pegar os N melhores pokémons por experiência
def get_n_best_pokemon_by_experience(df, top_n):
    return df.nlargest(top_n, "Experiência")

def generate_top_pokemon_interactive_bar(df, top_n=10):
    top_pokemons = df.nlargest(top_n, "Experiência")
    fig = px.bar(
        top_pokemons,
        x="Nome",
        y="Experiência",
        hover_data=["Imagem"],  # Dados adicionais para o hover
        text="Experiência",  # Mostra o valor em cada barra
        title="Top Pokémons por Experiência",
        labels={"Experiência": "Experiência", "Nome": "Pokémon"}
    )
    
    # Adiciona imagens nas tooltips
    fig.update_traces(
        hovertemplate=(
            "<b>%{x}</b><br>" +
            "Experiência: %{y}<br>" +
            "<img src='%{customdata}' style='max-height:100px; max-width:100px;'>"
        ),
        customdata=top_pokemons["Imagem"]  # Adiciona URLs das imagens no hover
    )
    
    # Ajusta layout
    fig.update_layout(
        xaxis=dict(title="Nome do Pokémon"),
        yaxis=dict(title="Experiência"),
        showlegend=False
    )
    
    return fig