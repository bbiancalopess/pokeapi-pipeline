# Pokémon Data Pipeline

Este projeto consome dados da PokeAPI, processa e gera insights.

## Configuração

1. Clone o repositório:
    ```bash
    git clone https://github.com/bbiancalopess/pokeapi-pipeline.git

    cd pokeapi-pipeline
    ```

A partir daqui você tem duas opções, rodar manualmente ou usar o docker. 

### Manualmente

1. Garanta que você tenha python e pip instalados. Você pode fazer isso tentando verificar a versão do python e do pip da sua máquina com os comandos
    ```bash
    python --version

    pip --version
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o script:
    ```bash
    python main.py
    ```

### Com o docker

1. Construa a imagem:
    ```bash
    docker build -t pokemon-pipeline .
    ```
2. Execute o container:
    ```bash
    docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/logs:/app/logs pokemon-pipeline
    ```

Ou, com Docker Compose:

1. Inicie o serviço:
    ``` bash
    docker-compose up
    ``` 


Os resultados estarão na pasta data/.