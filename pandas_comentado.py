# Importa a biblioteca pandas e a renomeia para 'pd' para facilitar o uso
# Pandas é uma biblioteca essencial para manipulação e análise de dados em Python, oferecendo estruturas como DataFrame e Series
import pandas as pd

### EXERCICIOS KEAGGLE
# 1.Creating, Reading and Writing
# In the cell below, create a DataFrame fruits that looks like this:

'''

   Apples  Bananas

0      30       21

'''

# Cria um DataFrame chamado 'fruits' usando um dicionário
# DataFrame é uma estrutura tabular bidimensional, como uma planilha, com linhas e colunas
# As chaves do dicionário se tornam os nomes das colunas ('Apples' e 'Bananas'), e os valores são listas com os dados
# O índice é gerado automaticamente começando de 0
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})

# Exibe o DataFrame 'fruits' para visualizar sua estrutura e dados
fruits

# Create a dataframe fruit_sales that matches the diagram below:

'''

            Apples  Bananas

2017 Sales      35       21

2018 Sales      41       34

'''

# Cria um DataFrame 'fruit_sales' com vendas de frutas para 2017 e 2018
# Define índices personalizados ('2017 Sales', '2018 Sales') usando o parâmetro 'index'
# Isso permite rótulos descritivos para as linhas, facilitando a interpretação
fruit_sales = pd.DataFrame({'Apples': [35,41], 'Bananas': [21,34]}, index=['2017 Sales','2018 Sales'])

# Exibe o DataFrame 'fruit_sales' para verificar se corresponde ao diagrama esperado
fruit_sales

# Create a variable ingredients with a Series that looks like:

'''

Flour     4 cups

Milk       1 cup

Eggs     2 large

Spam       1 can

Name: Dinner, dtype: object

'''

# Cria uma Series chamada 'ingredients' para representar ingredientes de uma receita
# Series é uma estrutura unidimensional, como uma coluna de dados
# Os valores são uma lista de quantidades, e o índice é uma lista de nomes dos ingredientes
# O parâmetro 'name' dá um nome à Series, útil para identificação
ingredients = pd.Series(['4 cups','1 cup','2 large','1 can'], index = ['Flour','Milk','Eggs','Spam'], name = 'Dinner')

# Exibe a Series 'ingredients' para visualizar os dados organizados
ingredients

# Read the following csv dataset of wine reviews into a DataFrame called reviews:

# The filepath to the csv file is ../input/wine-reviews/winemag-data_first150k.csv. The first few lines look like:

# Lê um arquivo CSV de avaliações de vinhos e cria um DataFrame 'reviews'
# pd.read_csv() é a função para ler arquivos CSV; 'index_col=0' define a primeira coluna como índice
# Isso carrega os dados em uma estrutura tabular para análise posterior
reviews = pd.read_csv('winemag-data_first150k.csv', index_col=0)

# Exibe o DataFrame 'reviews' para ver as primeiras linhas e entender a estrutura dos dados
reviews

# Cria um DataFrame 'animals' com dados de vacas e cabras ao longo de dois anos
# Índices personalizados ('Year 1', 'Year 2') facilitam a leitura dos dados por ano
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])

# Exibe o DataFrame 'animals' para visualizar os dados criados
animals

# Salva o DataFrame 'animals' em um arquivo CSV chamado 'cows_and_goats.csv'
# to_csv() é o método para exportar DataFrames para CSV; o nome do arquivo é passado como argumento
# Isso permite armazenar os dados em disco para uso futuro ou compartilhamento
animals.to_csv('cows_and_goats.csv')

# 2.Indexing, Selecting & Assigning
# Nesta seção, trabalharemos com o conjunto de dados Wine Reviews para praticar indexação, seleção e atribuição

# Lê novamente o arquivo CSV de avaliações de vinhos, definindo a primeira coluna como índice
# Isso garante que o DataFrame esteja pronto para operações de indexação
reviews = pd.read_csv('winemag-data_first150k.csv', index_col=0)

# Exibe as primeiras linhas do DataFrame 'reviews' usando head()
# head() mostra as primeiras 5 linhas por padrão, útil para inspecionar a estrutura dos dados
reviews.head()

# Seleciona a coluna 'description' do DataFrame 'reviews' e atribui à variável 'desc'
# Isso cria uma Series contendo todas as descrições dos vinhos
desc = reviews.description

# Alternativa: Seleciona a coluna 'description' usando notação de colchetes
# Ambas as formas são equivalentes para acessar colunas em DataFrames
desc = reviews['description']

# Seleciona o primeiro valor da coluna 'description' usando indexação posicional
# [0] acessa o primeiro elemento da Series, correspondendo ao primeiro vinho
first_description = reviews['description'][0]

# Alternativa: Acessa o primeiro elemento da coluna 'description' diretamente
# Funciona da mesma forma, pois 'description' é uma Series
first_description = reviews.description[0]

# Exibe o primeiro valor da descrição para visualização
first_description

# Seleciona a primeira linha completa do DataFrame 'reviews' usando iloc
# iloc[0] retorna a primeira linha (índice 0) como uma Series, útil para ver todos os dados de um registro
first_row = reviews.iloc[0]

# Exibe a primeira linha para inspecionar os dados do primeiro vinho
first_row

# Seleciona os primeiros 10 valores da coluna 'description' usando loc com fatiamento
# loc[:9, 'description'] seleciona linhas de 0 a 9 (inclusive) da coluna 'description'
first_descriptions = reviews.loc[:9, 'description']

# Alternativa: Usa iloc para selecionar os primeiros 10 elementos da coluna 'description'
# iloc[:10] seleciona os primeiros 10 elementos (0 a 9), já que iloc é exclusivo no final
first_descriptions = reviews.description.iloc[:10]

# Exibe as primeiras 10 descrições como uma Series
first_descriptions

# Seleciona registros específicos com índices 1, 2, 3, 5 e 8 usando iloc com lista
# iloc[[1,2,3,5,8]] retorna um DataFrame com essas linhas específicas
sample_reviews = reviews.iloc[[1,2,3,5,8]]

# Exibe o DataFrame com as amostras selecionadas
sample_reviews

# Cria um DataFrame 'df' contendo colunas específicas de linhas selecionadas
# loc[[0,1,10,100], ['country', 'province', 'region_1', 'region_2']] seleciona linhas e colunas específicas
df = reviews.loc[[0,1,10,100],['country', 'province', 'region_1', 'region_2']]

# Exibe o DataFrame 'df' com os dados selecionados
df

# Cria um DataFrame 'df' com as colunas 'country' e 'variety' dos primeiros 100 registros
# loc[:99, ['country', 'variety']] seleciona linhas 0 a 99 (inclusive) e as colunas especificadas
df = reviews.loc[:99,['country', 'variety']]

# Alternativa: Usa iloc para selecionar as primeiras 100 linhas e colunas por posição
# [0,11] refere-se às colunas na posição 0 ('country') e 11 ('variety')
df = reviews.iloc[:100, [0,11]]

# Exibe o DataFrame 'df' com os primeiros 100 registros
df

# Cria um DataFrame 'italian_wines' filtrando vinhos da Itália
# reviews.country == 'Italy' cria uma máscara booleana; loc[] aplica o filtro
italian_wines = reviews.loc[reviews.country == 'Italy']

# Alternativa: Filtragem direta sem loc, que também funciona para seleção condicional
italian_wines = reviews[reviews.country == 'Italy']

# Cria um DataFrame 'top_oceania_wines' com vinhos da Austrália ou Nova Zelândia com pontuação >= 95
# isin(['Australia','New Zealand']) verifica se o país está na lista; & combina condições
top_oceania_wines = reviews.loc[(reviews.country.isin(['Australia','New Zealand'])) & (reviews.points >= 95)]

# Exibe o DataFrame com os melhores vinhos da Oceania
top_oceania_wines

# 3.Summary Functions and Maps
# Nesta seção, exploramos funções de resumo e mapeamento para analisar dados de forma eficiente

# Calcula a mediana da coluna 'points' no DataFrame 'reviews'
# median() retorna o valor central quando os dados são ordenados, útil para entender a distribuição central
median_points = reviews.points.median()

# Obtém uma lista de países únicos representados no conjunto de dados
# unique() remove duplicatas, mostrando apenas valores distintos na coluna 'country'
countries = reviews.country.unique()

# Conta quantas vezes cada país aparece no conjunto de dados
# value_counts() cria uma Series com contagens, indexada pelos valores únicos
reviews_per_country = reviews.country.value_counts()

# Cria uma variável 'centered_price' subtraindo a média dos preços
# Isso centraliza os dados em torno de zero, útil para algoritmos de ML que assumem distribuição normal
centered_price = reviews.price - reviews.price.mean()

# Encontra o vinho com a melhor relação pontos/preço (melhor barganha)
# idxmax() retorna o índice do valor máximo; divide pontos por preço para obter a razão
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

# Conta quantas vezes as palavras "tropical" e "fruity" aparecem nas descrições
# map() aplica uma função lambda a cada descrição; sum() conta True como 1
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

# Exibe a contagem de descritores para comparar frequência
descriptor_counts

# Converte o sistema de pontuação (80-100) em estrelas (1-3) para simplificar
# Vinhos canadenses recebem automaticamente 3 estrelas devido a publicidade

# Cria uma nova coluna 'star_ratings' inicializada com 0
reviews['star_ratings'] = 0

# Atribui estrelas baseado em pontos: 3 para >=95, 2 para 85-94, 1 para <85
reviews['star_ratings'].loc[(reviews.points >= 85) & (reviews.points < 95)] = 2
reviews['star_ratings'].loc[reviews.points >= 95] = 3
reviews['star_ratings'].loc[reviews.points < 85] = 1

# Vinhos canadenses recebem 3 estrelas independentemente da pontuação
reviews['star_ratings'].loc[reviews.country == 'Canada'] = 3

# Extrai a Series de estrelas para uso posterior
star_ratings = reviews['star_ratings']

# Exibe o DataFrame atualizado com a nova coluna
reviews

# Abordagem alternativa usando apply() para criar estrelas
# apply() aplica uma função a cada linha (axis='columns') ou coluna

def stars(row):
    # Função que determina estrelas baseado em país e pontos
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

# Aplica a função stars a cada linha do DataFrame
star_ratings = reviews.apply(stars, axis='columns')

# 4.Grouping and Sorting
# Nesta seção, exploramos agrupamento e ordenação para analisar padrões nos dados

# Conta quantas avaliações cada degustador escreveu usando groupby
# groupby() agrupa dados por categoria; count() conta valores não-nulos em cada grupo
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

# Alternativa: size() conta todas as linhas em cada grupo, incluindo valores nulos
# Ambas as abordagens funcionam, mas size() é mais eficiente para contagem simples
reviews_written = reviews.groupby('taster_twitter_handle').size()

# Encontra a melhor pontuação para cada preço disponível
# Agrupa por preço, encontra o máximo de pontos em cada grupo, e ordena por preço
best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

# Calcula preços mínimo e máximo para cada variedade de vinho
# agg([min, max]) aplica múltiplas funções de agregação simultaneamente
price_extremes = reviews.groupby(['variety']).price.agg([min, max])

# Ordena variedades por preço mínimo e máximo em ordem decrescente
# sort_values() ordena o DataFrame; ascending=False para ordem decrescente
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

# Calcula a pontuação média dada por cada degustador
# Agrupa por nome do degustador e calcula a média dos pontos
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()

# Conta combinações mais comuns de país e variedade
# Agrupa por múltiplas colunas criando um MultiIndex; size() conta ocorrências
country_variety_counts = reviews.groupby(['country','variety']).size().sort_values(ascending=False)

# 5.Data Types and Missing Values
# Nesta seção, trabalhamos com tipos de dados e tratamento de valores ausentes

# Verifica o tipo de dados da coluna 'points'
# dtype retorna o tipo de dados da Series, importante para operações numéricas
dtype = reviews.points.dtype

# Converte os valores da coluna 'points' para strings
# astype() muda o tipo de dados; útil quando precisamos manipular dados como texto
point_strings = reviews.points.astype('str')

# Conta quantas avaliações estão sem preço (valores nulos)
# isnull() cria máscara booleana; filtragem mostra apenas linhas com preço nulo
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)

# Alternativa elegante: soma a Series booleana diretamente
# True é tratado como 1, False como 0; muito eficiente para contagem
n_missing_prices = reviews.price.isnull().sum()

# Conta regiões produtoras mais comuns, tratando valores ausentes
# fillna() substitui NaN por "Unknown"; value_counts() conta ocorrências por categoria
reviews_per_region = reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending=False)

# 6.Renaming and Combining
# Nesta seção, exploramos renomeação de colunas e combinação de DataFrames

# Exibe as primeiras linhas do DataFrame para visualizar a estrutura atual
# head() mostra as primeiras 5 linhas por padrão, útil para inspecionar dados
reviews.head()

# Renomeia colunas pouco descritivas para nomes mais claros
# rename() permite alterar nomes de colunas ou índices; copy() cria uma cópia independente
renamed = reviews.rename(columns={'region_1': 'region', 'region_2': 'locale'}).copy()

# Define o nome do índice (linhas) como 'wines' para maior clareza
# rename_axis() nomeia o índice, facilitando a interpretação do DataFrame
reindexed = reviews.rename_axis("wines", axis='rows')

# Carrega dados de produtos mencionados em subreddits do Reddit
# Esses dados vêm de fóruns específicos: gaming e movies

from pathlib import Path

gaming_products = pd.read_csv("top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"

movie_products = pd.read_csv("top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

# Combina DataFrames de diferentes subreddits usando concatenação
# concat() une DataFrames verticalmente (linhas); útil para combinar dados similares
combined_products = pd.concat([gaming_products, movie_products])

# Exibe o DataFrame combinado para verificar a união dos dados
combined_products

# Carrega dados do banco de dados de powerlifting do Kaggle
# Duas tabelas separadas: encontros (meets) e competidores

powerlifting_meets = pd.read_csv("openpowerlifting-meets.csv", alocate_memory=True)
powerlifting_competitors = pd.read_csv("openpowerlifting.csv")

# Combina as tabelas usando join baseado em MeetID
# set_index() define MeetID como índice; join() combina baseado no índice comum
left = powerlifting_meets.set_index(['MeetID'])
right = powerlifting_competitors.set_index(['MeetID'])

# Realiza o join para criar um DataFrame combinado
# left.join(right) combina dados de encontros com dados de competidores
powerlifting_combined = left.join(right)
