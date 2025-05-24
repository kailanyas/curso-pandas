# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv")
df.head()

#%%

# valores > 50
filtro = df["qtdePontos"] >= 50
df[filtro]

# %%

filtro = (df["qtdePontos"] >= 50) & (df["qtdePontos"] < 100)
#ou: (df["qtdePontos"] >= 50) * (df["qtdePontos"] < 100)

df[filtro]

# %%
filtro = (df["qtdePontos"] == 10) | (df["qtdePontos"] == 100)
df[filtro]