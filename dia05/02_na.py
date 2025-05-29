# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

# %%

# remover todas as linhas que possui nan
clientes.dropna()

# %%

# criando regras pra excluir nan 
clientes.dropna(how="all") #all: a linha inteira tem que ser nan

clientes.dropna(how="any") #any: se tiver ao menos um nan

# %%

df = pd.DataFrame(
    {
        "nome": ["Teo", None, "Thiago", "Nah"],
        "idade": [None, None, 22, 52],
        "salario": [3424, 6533, None, 2139]
    }
)

# trabalhando com nas -> filtrar quando a idade for na [criterio usado: idade]
df.dropna(how="all", subset=["idade"])

# criterio: idade, salario -> ambos tem que ser na por ter how=all
df.dropna(how="all", subset=["idade", "salario"])

# # criterio: idade, salario -> ao menos uma tem que ser na por ter how=all
df.dropna(how="any", subset=["idade", "salario"])

# %%

# preencher/inputar valores que são nan 
df["idade"].fillna(0) #uma serie especifica
df.fillna(0) #df inteiro

# com criterio pra cada coluna
df.fillna({"nome": "alguem", "idade": 0})

# input pela media
medias = df[["idade", "salario"]].mean()
df.fillna(medias)