# %%

# lista de idades
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

# calculando media e variancia dos valores de uma lista [sem utilizar series do pandas]
media = sum(idades) / len(idades)
print("Media:", media)

diffs = 0
for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades)-1)

print("Variância:", variancia)

# %%

import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

# armazenando os dados em uma series [com pandas]
series_idades = pd.Series(idades)
series_idades 


# %%

# calculando a media e variancia com o metodo 'mean' e 'var'
media_idades = series_idades.mean()
var_idades = series_idades.var()

# retorna informacoes/estatisticas das series, como count, media, desvio-padrao, etc
summary_idades = series_idades.describe()
summary_idades
