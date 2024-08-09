import pandas as pd
import statistics as st

df = pd.read_csv("assets/manutencao_preditiva.csv")

print(df)


df_filtrado = df[df["Tipo"] == "M"]
print(df_filtrado)

min = df["Temperatura Ar [K]"] == df_filtrado["Temperatura Ar [K]"].min()
print(min)