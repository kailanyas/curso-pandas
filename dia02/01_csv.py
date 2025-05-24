# %%
import pandas as pd

#importando dados de um arquivo csv
df = pd.read_csv("../data/clientes.csv")
df

# %%

#salvando vários tipos de arquivos
df.to_csv("teste.csv")

df.to_csv("teste.csv", index=False)
df.to_parquet("teste.parquet", index=False) ## arquivo binario
df.to_excel("teste.xlsx", index=False)
