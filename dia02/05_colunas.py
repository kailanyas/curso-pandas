# %%
import pandas as pd

df = pd.read_csv("../data/transacoes.csv")

#renomeando colunas
df = df.rename(columns={"qtdePontos": "qtPontos"}) #dicionario columns -> chave: nome antigo, valor: novo nome

df
# %%

# outra forma

renamed_columns = {
    "qtdePontos": "qtPontos",
    "descSistemaOrigem": "sistemaOrigem"
}

df.rename(columns=renamed_columns, inplace=True)
df

# %%

# acessando mais de uma coluna
df[["idCliente", "qtPontos"]]  

#ou

colunas = ["idCliente", "qtPontos"]
df[colunas]

# %%

#ordenando colunas -> ordem alfabética
colunas = list(df.columns)
colunas.sort()
df = df[colunas]
df