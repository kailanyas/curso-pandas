# %%
import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv")
df.head()

# %%

#operação com escalar em uma coluna -> criando nova coluna
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

df["todasSocial"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
df.head()

# %%

#descreve a coluna -> media, desvio padrao, etc
df["qtdePontos"].describe()

# %%

# aplicando log na coluna -> usa numpy (np é bom pra aplicar funcoes matematicas)
df["logPontos"] = np.log(df["qtdePontos"] + 1) #+1 evita log0 ; log deixa a distribuição MENOS assimetrica

# %%

# mostrando o efeito do log em graficos
import matplotlib.pyplot as plt

graficoPontos = plt.hist(df["qtdePontos"])
plt.grid(True)
plt.show()

#parece mais com uma distribuiçao normal
plt.hist(df["logPontos"])
plt.grid(True)
plt.show()

