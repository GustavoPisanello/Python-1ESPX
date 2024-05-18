import pandas as pd
import statistics as st
import matplotlib.pyplot as plt

df = pd.read_csv("assets/manutencao_preditiva.csv")

x = df["UDI"]
y1 = df["Temperatura Ar [K]"]
y2 = df["Temperatura Processo [K]"]

plt.plot(x, y1)
plt.xlabel("Amostras")
plt.ylabel("Temperaturas")
plt.title("Curvas de temperatura")

plt.show()

print(df["Tipo"].value_counts())

print(df[df["Tipo"] == "L"])

print(df)