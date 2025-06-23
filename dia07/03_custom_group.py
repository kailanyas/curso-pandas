#%%
#%%
import pandas as pd
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

# %%
def diff_amp(x: pd.Series):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude-media)**2)


# %%
(transacoes.groupby(by=["idCliente"], as_index=False)
           .agg({
               "idTransacao": ["count"],
               "qtdePontos": ["sum", "mean", diff_amp]
           })
)

# %%

#vendo a diferença de dias de um cliente
def life_time(x: pd.Series):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days

summary = (transacoes.groupby(by=["idCliente"], as_index=False)
           .agg({
               "idTransacao": ["count"],
               "qtdePontos": ["sum", "mean", diff_amp],
               "dtCriacao": [life_time]
           })
)

summary.columns = ["idClientes", "qtdeTransacao", "totalPontos", "mediaPontos", "ampMeanDiff", "lifeTime"]
summary
