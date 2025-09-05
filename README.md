# Curso de Pandas - Kaggle Learn

Este repositório contém os exercícios e soluções do curso de Pandas oferecido pela plataforma Kaggle Learn. O curso abrange desde conceitos básicos até técnicas avançadas de manipulação e análise de dados usando a biblioteca Pandas do Python.

## 📚 Conteúdo do Curso

### 1. Creating, Reading and Writing
- Criação de DataFrames e Series
- Leitura de arquivos CSV
- Salvamento de dados em disco
- Estruturas básicas do Pandas

**Conceitos Abordados:**
- `pd.DataFrame()` - Criação de tabelas bidimensionais
- `pd.Series()` - Criação de estruturas unidimensionais
- `pd.read_csv()` - Leitura de arquivos CSV
- `to_csv()` - Exportação para CSV

### 2. Indexing, Selecting & Assigning
- Seleção de dados por índice e posição
- Filtragem condicional
- Atribuição de valores
- Trabalho com índices customizados

**Técnicas Principais:**
- `iloc[]` - Seleção por posição
- `loc[]` - Seleção por rótulo
- Filtragem booleana
- `isin()` - Verificação de valores em listas

### 3. Summary Functions and Maps
- Funções estatísticas descritivas
- Transformação de dados
- Mapeamento de valores
- Análise de distribuições

**Funções Estatísticas:**
- `median()`, `mean()`, `min()`, `max()`
- `unique()`, `value_counts()`
- `map()`, `apply()`
- Operações vetorizadas

### 4. Grouping and Sorting
- Agrupamento de dados
- Operações de agregação
- Ordenação de resultados
- Análise por categorias

**Operações de Grupo:**
- `groupby()` - Agrupamento por categorias
- `agg()` - Múltiplas funções de agregação
- `sort_values()` - Ordenação de dados
- MultiIndex para agrupamentos complexos

### 5. Data Types and Missing Values
- Tipos de dados no Pandas
- Identificação de valores ausentes
- Estratégias de tratamento de dados faltantes
- Conversão entre tipos

**Tratamento de Dados:**
- `astype()` - Conversão de tipos
- `isnull()`, `isna()` - Detecção de valores nulos
- `fillna()` - Preenchimento de valores ausentes
- Verificação de integridade dos dados

### 6. Renaming and Combining
- Renomeação de colunas e índices
- Combinação de DataFrames
- Operações de junção
- Concatenação de dados

**Operações de Combinação:**
- `rename()` - Renomeação de elementos
- `concat()` - Concatenação vertical/horizontal
- `join()` - Junção baseada em índices
- `merge()` - Junção baseada em colunas

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
