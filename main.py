import pandas as pd

arquivo = r"tab_uso.xlsx"
df = pd.read_excel(arquivo)
print(df.info())


df["Importancia TransPub"] = ((df["Produzidas"] + df["Atraidas"]) / 2).round()
df["Importancia Infra"] = (
    df["População"] + df["Escolares"] * 1 / 3 + df["Empregos"]
).round()

# utilizei peso em regiões escolares

df.iloc


print(df.loc[df["Nome"] == "Freguesia do Ó"])


# vou estipular o custo
custoHora = 1
usoDia = 10
diasMes = 30
custoAnual = custoHora * usoDia * diasMes * 12

print(custoAnual)
print('Menos de 10 reais por dia, mais ou menos: "0.5 refeições"')

"""
    vou atribuir valor de 1 real por hora em bairros pequenos que conheço
    lembrando que esses valores, vão servir apenas para os 3 primeiros meses
    de lançamento
"""

df["valorRegiao"] = (
    (df["Importancia TransPub"] + df["Importancia Infra"]) / 100000
).round(decimals=2)

print(df.head())


"""
Agora vou criar a ia
"""


"""
=============================================
=============================================
=============================================
"""


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = df[["Importancia TransPub", "Importancia Infra"]].values
y = df["valorRegiao"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Erro quadrático médio (MSE):", mse)
print("Coeficiente de determinação (R²):", r2)


print("Coeficientes do modelo:", model.coef_)
