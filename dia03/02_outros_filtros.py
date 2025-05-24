# %%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv")
df.head()

# %%

filtro = (df["idProduto"] == 5) | (df["idProduto"] == 11)
df[filtro]

# %%

filtro = df["idProduto"].isin([5, 11])
df[filtro]

# %%

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

# valores nulos
clientes["dtCriacao"].isna() 

#negacao da afirmacao
~clientes["dtCriacao"].isna() 
 