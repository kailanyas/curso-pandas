# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df.head()

# %%

#operação aritmética em uma coluna -> criando nova coluna
df["pontos_100"] = df["qtdePontos"] + 100
df

# %%

#operacao entre duas colunas (um OU outro)
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

# %%

#operacao entre duas colunas (um E outro)
df["emailETwitch"] = df["flEmail"] * df["flTwitch"]
df.head()

# %%

#operacoes entre varias colunas
df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
df.head()



