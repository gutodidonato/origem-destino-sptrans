import pandas as pd

arquivo = r"tab_uso.xlsx"
df = pd.read_excel(arquivo)
print(df.info())


df["Importancia TransPub"] = (df["Produzidas"] + df["Atraidas"]) / 2
df["Importancia Infra"] = df["População"] + df["Escolares"] * 1 / 3 + df["Empregos"]
# utilizei peso em regiões escolares


print(df.head(5))
