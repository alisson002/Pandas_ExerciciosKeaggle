# Curso de Pandas - Kaggle Learn

Este repositório contém os exercícios e soluções do curso de Pandas oferecido pela plataforma Kaggle Learn. O curso abrange desde conceitos básicos até técnicas avançadas de manipulação e análise de dados usando a biblioteca Pandas do Python.

## 📚 Conteúdo do Curso

### 1. Creating, Reading and Writing
- Criação de DataFrames e Series
- Leitura de arquivos CSV
- Salvamento de dados em disco
- Estruturas básicas do Pandas

## 📚 Conteúdo do Curso

### 1. Creating, Reading and Writing
- Criação de DataFrames e Series
- Leitura de arquivos CSV
- Salvamento de dados em disco
- Estruturas básicas do Pandas

**Conceitos Abordados:**

- **`pd.DataFrame()`** - Criação de tabelas bidimensionais
  
  Função fundamental para criar DataFrames (estruturas tabulares 2D) no pandas. Aceita diversos tipos de entrada como dicionários, listas de listas, arrays NumPy ou outros DataFrames. Quando usado com dicionário, as chaves se tornam nomes das colunas e os valores (listas ou arrays) formam os dados das colunas. Permite definir índices customizados através do parâmetro `index=` e especificar tipos de dados com `dtype=`. É a base para análise de dados estruturados no pandas.
  
  Exemplo: `pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['linha1', 'linha2'])`

- **`pd.Series()`** - Criação de estruturas unidimensionais
  
  Constrói objetos Series (arrays unidimensionais rotulados) que funcionam como colunas de DataFrames ou estruturas independentes. Aceita listas, arrays, dicionários ou valores escalares. O parâmetro `index=` define rótulos personalizados para os elementos, enquanto `name=` nomeia a Series. Series são fundamentais no pandas pois suportam operações vetorizadas, indexação por rótulos e integração com DataFrames. Automaticamente alinha dados baseado no índice durante operações.
  
  Exemplo: `pd.Series([10, 20, 30], index=['a', 'b', 'c'], name='valores')`

- **`pd.read_csv()`** - Leitura de arquivos CSV
  
  Função versátil para ler arquivos CSV e convertê-los em DataFrames. Oferece múltiplos parâmetros: `sep=` para definir delimitadores, `header=` para especificar linha de cabeçalho, `index_col=` para definir coluna como índice, `usecols=` para selecionar colunas específicas, `dtype=` para forçar tipos de dados, `na_values=` para definir valores considerados nulos, `skiprows=` para pular linhas, `nrows=` para limitar quantidade de linhas lidas. Detecta automaticamente tipos de dados e lida com diferentes formatos de arquivo.
  
  Exemplo: `pd.read_csv('arquivo.csv', index_col=0, dtype={'coluna': 'str'}, na_values=['N/A'])`

- **`to_csv()`** - Exportação para CSV
  
  Método para salvar DataFrames ou Series em arquivos CSV. Principais parâmetros: `path_or_buf=` define nome/caminho do arquivo, `sep=` especifica delimitador, `index=` controla se índice é incluído (True/False), `header=` controla inclusão de cabeçalho, `columns=` seleciona colunas específicas para exportar, `na_rep=` define representação de valores nulos, `encoding=` especifica codificação de caracteres. Preserva estrutura e tipos de dados para posterior reimportação.
  
  Exemplo: `df.to_csv('saida.csv', index=False, sep=';', na_rep='VAZIO')`

### 2. Indexing, Selecting & Assigning
- Seleção de dados por índice e posição
- Filtragem condicional
- Atribuição de valores
- Trabalho com índices customizados

**Técnicas Principais:**

- **`iloc[]` - Seleção por posição INTEGER-LOCATION**
  
  Seletor baseado exclusivamente em posições numéricas (integers), ignorando completamente os rótulos do índice. Utiliza indexação baseada em zero como listas Python. Sintaxe: `df.iloc[linhas, colunas]` onde linhas e colunas são posições numéricas. Aceita números únicos (`df.iloc[0, 1]`), fatias (`df.iloc[0:3, 1:4]`), listas (`df.iloc[[0, 2], [1, 3]]`) ou máscaras booleanas. **CRUCIAL: fatias com iloc são EXCLUSIVAS no final** (Python padrão) - `iloc[0:3]` retorna posições 0, 1, 2 (3 elementos). Ideal quando você conhece posições exatas ou quer selecionar por ordem relativa.
  
  Exemplos críticos:
  - `df.iloc[0:5]` → retorna 5 linhas (posições 0,1,2,3,4)  
  - `df.iloc[:, -1]` → última coluna
  - `df.iloc[[0,2,4], 1:3]` → linhas específicas, colunas 1 e 2

- **`loc[]` - Seleção por rótulo LABEL-LOCATION**
  
  Seletor baseado em rótulos/índices nomeados, considerando os nomes reais das linhas e colunas. Sintaxe: `df.loc[índices, colunas]` usando nomes/rótulos reais. **FUNDAMENTAL: fatias com loc são INCLUSIVAS em ambos os extremos** - diferente do comportamento padrão Python. Se DataFrame tem índices 0,1,2,3,4, então `df.loc[0:3]` retorna posições 0,1,2,3 (4 elementos). Aceita nomes únicos, fatias de nomes, listas de nomes, condições booleanas. É o método preferido para seleção quando você trabalha com índices significativos.
  
  **DIFERENÇAS CRÍTICAS iloc vs loc:**
  ```python
  df = pd.DataFrame({'A':[1,2,3,4,5]}, index=[10,20,30,40,50])
  
  df.iloc[0:3] # Retorna índices 10,20,30 (3 linhas) - exclusivo
  df.loc[10:30] # Retorna índices 10,20,30 (3 linhas) - inclusivo
  df.loc[10:40] # Retorna índices 10,20,30,40 (4 linhas) - inclusivo!
  ```
  
  loc é mais intuitivo para dados com índices significativos, iloc para posições absolutas.

- **Filtragem booleana**
  
  Técnica poderosa usando condições lógicas para filtrar dados. Cria máscaras booleanas (Series de True/False) aplicadas ao DataFrame. Operadores de comparação (`==`, `!=`, `>`, `<`, `>=`, `<=`) geram máscaras elemento por elemento. Operadores lógicos para combinar condições: `&` (AND), `|` (OR), `~` (NOT) - **obrigatório usar parênteses** pois têm precedência alta. Sintaxe: `df[condição]` ou `df.loc[condição]`. Permite filtragem dinâmica baseada nos próprios dados.
  
  Exemplos: `df[df['idade'] > 18]`, `df[(df['nome'] == 'João') & (df['idade'] < 30)]`

- **`isin()` - Verificação de valores em listas**
  
  Método que verifica se valores de uma Series/coluna estão contidos em uma lista, tupla ou conjunto específico. Retorna máscara booleana True para valores encontrados, False para não encontrados. Equivale a múltiplas comparações OR mas de forma otimizada. Útil para filtrar múltiplos valores específicos sem usar várias condições OR. Também funciona com outros tipos de sequências e até outros DataFrames/Series para verificações mais complexas.
  
  Exemplo: `df[df['pais'].isin(['Brasil', 'Argentina', 'Chile'])]` filtra apenas esses três países.

### 3. Summary Functions and Maps
- Funções estatísticas descritivas
- Transformação de dados
- Mapeamento de valores
- Análise de distribuições

**Funções Estatísticas:**

- **`median()`, `mean()`, `min()`, `max()`** - Estatísticas descritivas básicas
  
  Funções agregadas fundamentais que calculam estatísticas resumidas dos dados. `median()` calcula valor central ordenado (robusto a outliers), `mean()` calcula média aritmética (sensível a outliers), `min()`/`max()` encontram valores extremos. Por padrão ignoram valores NaN. Parâmetro `axis=` controla direção: `axis=0` (padrão) calcula ao longo das linhas (resultado por coluna), `axis=1` calcula ao longo das colunas (resultado por linha). `skipna=False` inclui NaN nos cálculos. Retornam Series quando aplicadas a DataFrame, escalares quando aplicadas a Series.

- **`unique()` - Valores únicos**
  
  Retorna array NumPy com valores únicos de uma Series, removendo duplicatas e preservando ordem de primeira ocorrência. Útil para explorar categorias ou valores distintos em colunas. Para DataFrames, deve ser aplicado coluna por coluna. Diferente de `drop_duplicates()` que trabalha com linhas completas. Mantém tipo de dados original e lida automaticamente com valores NaN (incluídos se existentes).
  
  Exemplo: `df['categoria'].unique()` → array(['A', 'B', 'C'])

- **`value_counts()` - Contagem de frequências**
  
  Calcula frequência de cada valor único em Series, retornando Series ordenada por contagem (decrescente por padrão). Parâmetros importantes: `normalize=True` retorna proporções ao invés de contagens, `sort=False` mantém ordem original, `ascending=True` ordena crescente, `bins=` cria intervalos para dados numéricos, `dropna=False` inclui valores nulos na contagem. Essencial para análise exploratória de dados categóricos e distribuições.
  
  Exemplo: `df['cor'].value_counts(normalize=True)` → proporções de cada cor

- **`map()` - Mapeamento de valores**
  
  Mapeia cada valor de uma Series usando dicionário, Series ou função, retornando nova Series transformada. Com dicionário/Series, substitui valores por correspondências exatas. Com função, aplica função a cada elemento individualmente. Valores não encontrados em mapeamentos tornam-se NaN por padrão. Diferente de `apply()`, `map()` é otimizado para transformações de valores simples elemento-por-elemento. Ideal para recodificação de categorias ou transformações baseadas em lookup tables.
  
  Exemplo: `s.map({'A': 1, 'B': 2})` ou `s.map(lambda x: x.upper())`

- **`apply()` - Aplicação de funções**
  
  Aplica função ao longo de um eixo de DataFrame ou a cada elemento de Series. Para DataFrame: `axis=0` aplica função a cada coluna, `axis=1` aplica a cada linha. Função pode ser lambda, função built-in ou função personalizada. Mais flexível que `map()` pois pode trabalhar com elementos individuais ou agregações. Para Series, aplica função elemento por elemento. Parâmetro `args=` passa argumentos adicionais à função. Base para transformações customizadas complexas.
  
  Exemplo: `df.apply(lambda col: col.max() - col.min())` → range de cada coluna

### 4. Grouping and Sorting
- Agrupamento de dados
- Operações de agregação
- Ordenação de resultados
- Análise por categorias

**Operações de Grupo:**

- **`groupby()` - Agrupamento por categorias**
  
  Operação fundamental que divide DataFrame em grupos baseado em valores de uma ou mais colunas, permitindo aplicar operações a cada grupo separadamente (split-apply-combine). Aceita nome de coluna, lista de colunas, função ou Series para critério de agrupamento. Retorna objeto GroupBy especial (não executa operação até chamar método agregador). Parâmetros importantes: `as_index=False` mantém colunas de agrupamento como colunas normais, `sort=False` mantém ordem original, `dropna=False` inclui grupos com NaN. Permite operações diferentes em colunas diferentes simultaneamente.
  
  Exemplo: `df.groupby(['pais', 'categoria'])` cria grupos para cada combinação única

- **`agg()` - Múltiplas funções de agregação**
  
  Aplica uma ou mais funções de agregação a dados agrupados ou DataFrame completo. Aceita função única (`'mean'`), lista de funções (`['mean', 'std']`), dicionário mapeando colunas para funções (`{'preco': 'mean', 'quantidade': 'sum'}`), ou funções customizadas. Retorna DataFrame/Series com resultados nomeados. Ideal para criar relatórios resumidos com múltiplas métricas simultaneamente. Combina-se perfeitamente com `groupby()` para análises complexas por categoria.
  
  Exemplo: `df.groupby('categoria').agg({'vendas': ['sum', 'mean'], 'lucro': 'max'})`

- **`sort_values()` - Ordenação de dados**
  
  Ordena DataFrame/Series por valores de uma ou mais colunas. Parâmetros principais: `by=` especifica coluna(s) para ordenação, `ascending=` controla direção (True=crescente, False=decrescente, pode ser lista para colunas múltiplas), `na_position=` define posição de valores nulos ('first' ou 'last'), `inplace=False` cria nova cópia por padrão, `key=` aplica função antes de ordenar. Para múltiplas colunas, ordena pela primeira coluna, depois pela segunda para quebrar empates, etc.
  
  Exemplo: `df.sort_values(['prioridade', 'data'], ascending=[False, True])`

- **MultiIndex - Índices hierárquicos**
  
  Estrutura de índice com múltiplos níveis (hierárquico) que permite organização complexa de dados multidimensionais. Criado automaticamente por `groupby()` com múltiplas colunas ou manualmente com `pd.MultiIndex.from_*()`. Navegação usando tuplas ou métodos específicos como `.loc[('nivel1', 'nivel2')]`. Métodos úteis: `reset_index()` converte níveis em colunas, `unstack()` converte nível de índice em colunas, `stack()` faz o inverso. Permite análise de dados com hierarquias naturais (tempo/região/categoria).

### 5. Data Types and Missing Values
- Tipos de dados no Pandas
- Identificação de valores ausentes
- Estratégias de tratamento de dados faltantes
- Conversão entre tipos

**Tratamento de Dados:**

- **`astype()` - Conversão de tipos**
  
  Converte tipos de dados de Series/DataFrame para tipos especificados. Aceita strings ('int64', 'float32', 'str', 'category'), tipos NumPy ou dicionário mapeando colunas para tipos. Parâmetro `errors=` controla comportamento com falhas: 'raise' (padrão, levanta exceção), 'ignore' (mantém tipo original). Útil para otimizar memória (int32 vs int64), converter strings em números, criar dados categóricos, ou preparar dados para algoritmos específicos. Validação automática verifica se conversão é possível.
  
  Exemplo: `df.astype({'idade': 'int32', 'nome': 'category', 'ativo': 'bool'})`

- **`isnull()`, `isna()` - Detecção de valores nulos**
  
  Funções idênticas que detectam valores ausentes/nulos em DataFrames ou Series, retornando máscara booleana (True=nulo, False=válido). Detectam NaN, None, pd.NaT (datas nulas) e pd.NA (tipo geral nulo). Para DataFrame, retorna DataFrame booleano da mesma forma. Combinam-se com `sum()` para contar nulos por coluna, `any()` para verificar existência de nulos, `all()` para verificar se tudo é nulo. Base para análise de completude dos dados e estratégias de limpeza.
  
  Exemplo: `df.isnull().sum()` conta nulos por coluna

- **`fillna()` - Preenchimento de valores ausentes**
  
  Substitui valores nulos por valores especificados usando diversas estratégias. Parâmetros principais: `value=` especifica valor de substituição (escalar, dicionário por coluna, Series), `method=` define método ('ffill' propaga último valor válido para frente, 'bfill' propaga próximo valor válido para trás), `limit=` limita número de preenchimentos consecutivos, `inplace=False` cria cópia por padrão. Permite estratégias sofisticadas como preenchimento por média, mediana ou valores específicos por grupo.
  
  Exemplo: `df.fillna({'idade': df['idade'].median(), 'nome': 'Desconhecido'})`

- **Verificação de integridade dos dados**
  
  Processo sistemático para identificar e corrigir problemas nos dados. Inclui: verificação de tipos apropriados (`dtypes`), detecção de outliers (`describe()`, quartis), consistência de dados (`duplicated()`, `drop_duplicates()`), completude (`info()`, `isnull().sum()`), ranges válidos (comparações condicionais), relações entre colunas. Métodos úteis: `info()` resume estrutura geral, `describe()` mostra estatísticas por coluna, `nunique()` conta valores únicos, `memory_usage()` analisa uso de memória.

### 6. Renaming and Combining
- Renomeação de colunas e índices
- Combinação de DataFrames
- Operações de junção
- Concatenação de dados

**Operações de Combinação:**

- **`rename()` - Renomeação de elementos**
  
  Renomeia índices ou colunas de DataFrames/Series usando mapeamentos flexíveis. Parâmetros: `columns=` para renomear colunas (dicionário ou função), `index=` para renomear índices, `mapper=` renomeia índice por padrão, `axis=` especifica eixo, `inplace=False` cria cópia por padrão, `level=` especifica nível em MultiIndex, `errors=` controla tratamento de chaves inexistentes. Função pode ser lambda para transformações sistemáticas. Essencial para padronizar nomes, corrigir typos ou adequar nomenclatura para análise.
  
  Exemplo: `df.rename(columns={'nome_antigo': 'nome_novo'}, index={0: 'primeira_linha'})`

- **`concat()` - Concatenação vertical/horizontal**
  
  Combina múltiplos DataFrames/Series ao longo de um eixo especificado. Parâmetros cruciais: `axis=0` concatena verticalmente (empilha linhas), `axis=1` concatena horizontalmente (adiciona colunas), `ignore_index=True` recria índice sequencial, `keys=` adiciona nível hierárquico identificando origem, `sort=False` mantém ordem das colunas, `join='outer'` mantém todas colunas ('inner' mantém apenas comuns). Ideal para combinar datasets com estrutura similar ou adicionar novos dados históricos.
  
  Exemplo: `pd.concat([df1, df2], axis=0, ignore_index=True)` empilha DataFrames

- **`join()` - Junção baseada em índices**
  
  Combina DataFrames usando índices como chave de junção (similar a SQL JOIN). Parâmetros: `how=` especifica tipo ('left', 'right', 'outer', 'inner'), `lsuffix=` e `rsuffix=` adicionam sufixos a colunas com nomes duplicados, `sort=False` mantém ordem do DataFrame esquerdo. Por padrão faz LEFT JOIN usando índice. Eficiente quando relacionamento natural existe entre índices dos DataFrames. Retorna novo DataFrame com colunas combinadas.
  
  Exemplo: `df1.join(df2, how='inner')` mantém apenas índices presentes em ambos

- **`merge()` - Junção baseada em colunas**
  
  Operação mais flexível para combinar DataFrames baseado em valores de colunas (equivale a SQL JOIN). Parâmetros essenciais: `on=` especifica colunas de junção (devem existir em ambos DataFrames), `left_on=` e `right_on=` usam colunas diferentes, `how=` define tipo de junção ('inner', 'outer', 'left', 'right'), `suffixes=` personaliza sufixos para colunas duplicadas, `validate=` verifica tipo de relacionamento ('1:1', '1:m', 'm:1'), `indicator=True` adiciona coluna mostrando origem de cada linha.
  
  Exemplo: `pd.merge(clientes, pedidos, on='cliente_id', how='left')` mantém todos clientes

## 🎯 Dataset Principal

O curso utiliza principalmente o **Wine Reviews Dataset**, que contém:
- 150.000 avaliações de vinhos
- Informações sobre país, região, variedade
- Pontuações de 80-100 pontos
- Preços e descrições detalhadas
- Dados de degustadores profissionais

## 🔧 Tecnologias e Ferramentas

- **Python 3.x** - Linguagem base
- **Pandas 1.5+** - Manipulação e análise de dados
- **NumPy** - Operações numéricas (dependência do Pandas)
- **Jupyter Notebook** - Ambiente de desenvolvimento interativo

### **Instalação Completa**
```bash
# Instalação básica
pip install pandas jupyter

# Para análise mais avançada (opcional)
pip install pandas jupyter matplotlib seaborn plotly

# Ou usando conda
conda install pandas jupyter notebook
```

### **Imports Essenciais**
```python
import pandas as pd

```

## 📊 Casos de Uso Práticos

1. **Análise de Mercado de Vinhos**
   - Identificação de melhores relações custo-benefício
   - Análise por região e país
   - Tendências de pontuação por degustador

2. **Processamento de Dados de E-commerce**
   - Combinação de dados de diferentes fontes (Reddit)
   - Análise de produtos por categoria

3. **Análise Esportiva**
   - Combinação de dados de competições e competidores
   - Análise de performance em powerlifting

## 🚀 Como Usar Este Repositório

1. **Clone o repositório:**
```bash
git clone https://github.com/alisson002/Pandas_ExerciciosKeaggle.git
cd Pandas_ExerciciosKeaggle
```

2. **Instale as dependências:**
```bash
pip install pandas jupyter
```

3. **Execute o Jupyter Notebook:**
```bash
jupyter notebook pandas.ipynb
```

## 🎯 Objetivos de Aprendizagem

Ao completar este curso, você será capaz de:

- ✅ Criar e manipular DataFrames e Series
- ✅ Realizar operações de seleção e filtragem complexas
- ✅ Aplicar funções estatísticas e de transformação
- ✅ Agrupar dados e realizar agregações
- ✅ Tratar dados ausentes e converter tipos
- ✅ Combinar múltiplas fontes de dados
- ✅ Realizar análises exploratórias completas

## 📚 Recursos Complementares

- [Documentação Oficial do Pandas](https://pandas.pydata.org/docs/)
- [Kaggle Learn - Pandas Course](https://www.kaggle.com/learn/pandas)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
