# %%

import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
dfs = pd.read_html(url) #retorna uma LISTA de tabelas da pagina
dfs  

# %%

#acessando a de interesse
df = dfs[1]
df

#salvando
df.to_csv("ufs.csv", sep=";", index=False)