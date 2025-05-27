# %%
import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")
clientes.head()

# %%

# ordena os valores (indices "desordenados")
clientes["qtdePontos"].sort_values()

# ordena o df pela qtdePontos -> sempre usar by
clientes.sort_values(by="qtdePontos", ascending=False).head()

#ordena o df pelos pontos e retorna uma serie dos pontos + id dos clientes
(clientes.sort_values(by="qtdePontos", ascending=False).head()["idCliente"])

# %%
teste = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario": [2345, 4533, 3245, 4533]
    }
)

# ordenando pelo salario e como criterio de desempate idade
teste.sort_values(by = ["salario", "idade"], ascending=False)

# fazendo salario ser crescente e idade descrecente
teste.sort_values(by = ["salario", "idade"], ascending=[False, True])
