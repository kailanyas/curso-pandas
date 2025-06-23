#%%
import pandas as pd

idades = [34, 33, 54, 12, 45, 23, 67, 34, 83, 39, 15, 52, 25]
idades = pd.Series(idades)
idades

# %%

# Agregação de dados: soma, minimo, máximo, media (calcular estatisticas)
idades.sum()
idades.min()
idades.max()
idades.mean()
idades.describe() #retorna uma lista de estatisticas

# %%
clientes = pd.read_csv("../data/clientes.csv")
clientes

#quantas pessoas tem a twitch?
clientes["flTwitch"].sum()

#proporcao de pessoas que tem a twitch?
clientes["flTwitch"].mean()

# %%
# quantas pessoas tem todas as redes sociais?
redes_sociais = ["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]
clientes[redes_sociais].mean() #aplica a média em cada uma das colunas do dataframe

# %%
#pegando os valores que nao sao object
num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.tolist() #pega as colunas numericas

clientes[num_columns].mean()
clientes[num_columns].describe()