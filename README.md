# Pokémon Data Pipeline

Este projeto consome dados da PokeAPI, processa e gera insights relacionados aos pokémons.

## Configuração

#### 1. Clone o repositório 
Para começar, clone o repositório e entre na pasta do projeto:

    ```bash
    git clone https://github.com/bbiancalopess/pokeapi-pipeline.git

    cd pokeapi-pipeline
    ```

#### 2. Opções de execução 
Você tem duas opções para rodar o projeto: manualmente ou com o Docker. 

### Execução manual

#### 1. Verifique se você tem o Python e o pip instalados 
Para garantir que o Python e o pip estão instalados corretamente na sua máquina, execute os seguintes comandos:

    ```bash
    python --version

    pip --version
    ```

Se ambos os comandos retornarem as versões instaladas, você pode continuar.

#### 2. Instale as dependências:
O projeto usa algumas bibliotecas externas que precisam ser instaladas. Para isso, execute:

    ```bash
    pip install -r requirements.txt
    ```

#### 3. Execute o script:
Com as dependências instaladas, basta rodar o script principal para iniciar o pipeline:

    ```bash
    python main.py
    ```

### Execução com Docker

#### 1. Construa a imagem Docker:
Se você optar por usar o Docker, primeiro é necessário construir a imagem. Para isso, execute:

    ```bash
    docker build -t pokemon-pipeline .
    ```

#### 2. Execute o container Docker:
Após a construção da imagem, você pode rodar o container com o seguinte comando:

    ```bash
    docker run --rm -v $(pwd)/data:/app/data -v $(pwd)/logs:/app/logs pokemon-pipeline
    ```

Isso criará volumes mapeados para as pastas data e logs no seu diretório local, onde os resultados e logs serão armazenados.

#### 3. Alternativa: Usando Docker Compose:
Se preferir usar o Docker Compose para gerenciar o container, siga os passos abaixo:
- Primeira execução (construindo imagem e iniciando o container):
    
    ```bash
    docker compose up --build
    ```

- Execuções subsequentes:
Para rodar o container novamente sem reconstruir a imagem, basta usar o comando:

    ```bash
    docker compose up
    ```

O Docker Compose facilita o gerenciamento do ambietne e garante que todas as dependências sejam carregadas de forma consistente.

### Resultados
Os resultados da execução (relatórios e gráficos) serão salvos na pasta data/ no seu diretório local, que é mapeado através do Docker.

### Logs
Os logs da execução são armazenados na pasta logs/, onde você pode acompanhar o progresso da execução e possíveis erros.

### Notas Finais
- Se estiver rodando o projeto manualmente, verifique se a versão do Python e das dependências está correta, pois o ambiente Docker já cuida disso.
- Caso enfrente algum erro relacionado à API ou aos dados, verifique os logs gerados para mais informações.