# %%
import pandas as pd

df = pd.read_html("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")
uf = df[1]
uf.head()

# %%

def str_to_float(x:str):
    return float(x.replace(" ", "").replace( ",",".").replace("\xa0", ""))
    return float(x)

# %%
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

# %%

# Trabalhando com a coluna expectativa de vida (string -> float)
def exp_to_anos(exp):
    return float(exp.replace(",", ".").replace(" anos", ""))

uf["Expectativa de vida (2016)"] = uf["Expectativa de vida (2016)"].apply(exp_to_anos)


# Trabalhando com a coluna mortalidade infantil (string -> float)
def mortalidade_to_float(x):
    x = float(x.replace("‰", "").replace(",", "."));
    return x

uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)

# %%
# apply no dataframe 

# aplicando em UMA linha
linha = uf.iloc[6]
(linha["PIB per capita (R$) (2015)"] > 20000 and linha["Mortalidade infantil (/1000)"] < 15 and linha["IDH (2010)"] > 700)

# generalizando:
def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 20000 and linha["Mortalidade infantil (/1000)"] < 15 and linha["IDH (2010)"] > 700)

#aplicando em cada linha do dataframe
uf.apply(classifica_bom, axis=1) #axis = 1 aplica linha a linha, axis = 0 aplica em cada coluna
