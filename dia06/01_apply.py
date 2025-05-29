# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")
df.head()

# %%

#EXEMPLO: tenho esse id e quero pegar a última parte: 47f581ec52a1
idCliente = "000ff655-fa9f-4baa-a108-47f581ec52a1"

# funcao para o problema
def get_last_id(x):
    return x.split("-")[-1]

# %%
# ----- FAZENDO S/ METODO APPLY -----

id_novo = []

for i in df["idCliente"]:
    novo = get_last_id(i);
    id_novo.append(novo)

df["novo_id"] = id_novo
df.head()

# %%

# ----- FAZENDO C/ METODO APPLY -----

df["idCliente"].apply(get_last_id) #apply: aplica transformacoes em todos elementos
