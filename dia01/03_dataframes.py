# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

nomes = [
    "Teo", "Maria", "Jose", "Luiz", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Tito"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df

# %%
# acessando o df
df["nomes"]

#acessando uma linha
df.iloc[0]["nomes"]
