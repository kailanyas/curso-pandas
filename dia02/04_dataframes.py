# %%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv")
df_clientes

# %%

# exibe as 5 primeiras linhas
df_clientes.head()

# %%

# exibe o final -> 5 ultimos por padrão
df_clientes.tail() 

# %%

# exibe amostra aleatoria
df_clientes.sample(10)

# %%

#obter o valor das linhas e colunas
df_clientes.shape

# %%

#obtendo o nome das colunas
df_clientes.columns

# %%

#obtendo os indices
df_clientes.index

# %%
df_clientes.info(memory_usage='deep') #deep -> pega a memoria real

# %%

df_clientes.dtypes #retorna uma serie com tipo de cada coluna
