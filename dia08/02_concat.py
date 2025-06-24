# %%
import pandas as pd

df = pd.DataFrame({
    "cliente": [1,2,3,4],
    "nome": ["teo", "nah", "thi", "ana"]
})

df_02 = pd.DataFrame({
    "cliente": [5,6,7,],
    "nome": ["kai", "hilary", "fran"],
    "idade":[32,29, 31]
})

df_03 = pd.DataFrame({
    "idade": [32,34,19,54]
})

# %%

#concat: "empilha" os df; adiciona um abaixo do outro
pd.concat([df, df_02], ignore_index=True) #reseta o indice (1, ..., n)

# %%

df_03 = df_03.sort_values(by = "idade")
df_03

# %%

pd.concat([df, df_03], axis=1) #axis = 1: empilha do lado (coloca do lado) ; concatena pelo INDICE (indices iguais)

# %%

# caso não queira que concatena pelo indice, é necessario reseta-lo:

df_03 = df_03.sort_values(by = "idade").reset_index(drop=True)
pd.concat([df, df_03], axis=1) 


