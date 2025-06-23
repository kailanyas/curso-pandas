# %%
#APRENDENDO A USAR MAIS DE UM DATAFRAME -> fazer operações entre dataframes [merge & concat]

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

# %%

#juntar duas base de dados:
transacoes.merge(right=clientes, 
                 how='left', # how = como vai fazer o merge (left = considera como referencia a tabela da esquerda, inner = considera so as linhas que estao em AMBAS as tabelas, right = usa como referencia a tabela da direita)
                 on='idCliente', #on = coluna em comum,
                 suffixes=["Transcao", "Cliente"] #suffixes = sufixo pra colunas repetidas
)

# %%

#exemplo: quando uma MESMA coluna tem nomes diferentes nos df
df_1 = pd.DataFrame(
    {
        "transacao": [1,2,3,4,5],
        "idCliente": [1,2,3,2,2],
        "valor": [10,34,46,53,87]
    }
)

df_2 = pd.DataFrame(
    {
        "id": [1,2,3,4],
        "valor": ["teo", "nah", "thi", "ana"]
    }
)

#left_on, right_on: especifica as colunas "chaves"
df_1.merge(df_2, left_on=["idCliente"], right_on=["id"], how="left")

# %%

#EXERCICIO: Quem teve mais transações de Streak (que é o produto)?

#importando df que precisamos usar
transacoes = pd.read_csv("../data/transacoes.csv")
transacoes.head()

transacao_produto = pd.read_csv("../data/transacao_produto.csv")
transacao_produto.head()

produtos =  pd.read_csv("../data/produtos.csv")
produtos.head()

cliente_transacao_produto = transacoes.merge(transacao_produto,
                 on="idTransacao",
                 how="left"                 
)

cliente_transacao_produto = cliente_transacao_produto[['idTransacao', 'idCliente', 'idProduto']]

df_full = cliente_transacao_produto.merge(
    produtos,
    on=['idProduto'],
    how = 'left'
)

df_full = df_full[df_full["descProduto"] == "Presença Streak"]

(df_full.groupby(by=['idCliente'])["idTransacao"]
        .count()
        .sort_values(ascending=False)
        .head(1)
)

# %%

# OUTRA FORMA DE RESOLVER O EXERCICIO

produtos = produtos[produtos["descProduto"] == "Presença Streak"]

(transacoes.merge(
    transacao_produto,
    on="idTransacao",
    how="left")
    .merge(produtos, on=["idProduto"], how="right")
    .groupby(by="idCliente")["idTransacao"]
    .count()
    .sort_values(ascending=False)
    .head(1)
)

