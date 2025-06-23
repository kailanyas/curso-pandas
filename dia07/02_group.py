#%%
import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

# %%

#(agrupando pelo cliente)
transacoes.groupby(by="idCliente").count() #by: pelo que vc quer agrupar? 

#quantas transacoes cada cliente teve?
transacoes.groupby(by="idCliente", as_index=False)[["idTransacao"]].count() #dois colchetes: retorna dataframe ; as_index -> tira a coluna de indice

# %%
#qtd_transacao, total_pontos e pontos/transacao
summary = (transacoes.groupby(by="idCliente", as_index=False)
            .agg({
                "idTransacao": ['count'],
                "qtdePontos": ['sum', 'mean']
            }))

summary.columns # multiIndex

# %%
#solucao para multiIndex (tratar de maneira mais facil)

summary.columns = ["idCliente", "qtdeTransacao", "totalPontos", "avgPontos"]
summary