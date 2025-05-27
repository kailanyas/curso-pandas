# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df.head()

# %%

# convertando valores para outro tipo -> astype
df["qtdePontos"].astype(float)

# %%

# converter para datas

#replace -> substituir valores (substitui 0000.. por 2024...)
df["dtCriacao"] = df["dtCriacao"].replace({"0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"})

# %%

# convertendo para data
pd.to_datetime(df["dtCriacao"])

# %%

# comum ver:

replace = {"0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"}

df["dtCriacao"] = pd.to_datetime(df["dtCriacao"].replace(replace))

# %%

# tendo tipos datas, há vários atributos -> year, day, month, month_name()
df["dtCriacao"].dt.year

# quando tenho NaN, o tipo da serie tem que ser float