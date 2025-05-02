
# %%
import pandas as pd

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

series_idades = pd.Series(idades)

# acesso a elementos
series_idades[0] #os indices da serie funcionam igual as chaves dos dicionarios

series_idades.iloc[0] #indice no sentido de posicao -> 32

series_idades.iloc[:3] #retorna os 3 primeiros elementos

# %%
idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 32
]

indexs = [
    "Teo", "Maria", "Jose", "Luiz", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Tito"
]

series_idades = pd.Series(idades, index=indexs) #os index se tornam a lista de nomes
series_idades["Pedro"] #retorna o numero associado ao nome Pedro
series_idades.iloc[0] #retorna a POSIÇÃO zero

