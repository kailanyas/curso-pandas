# %%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

# %%
# Exercicio 05.05 - Selecione a primeira transação diária de cada cliente

transacoes = transacoes.sort_values("dtCriacao")
transacoes["data"] = pd.to_datetime(transacoes["dtCriacao"]).dt.date
transacoes.drop_duplicates(keep="first", subset=["idCliente", "data"])