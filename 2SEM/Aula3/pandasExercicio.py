import pandas as pd

#Exercício 1
s1 = pd.Series((range(1, 11)), name = "Serie 1\n")

print(f"{s1[2]}\n")

#Exercício 2

s2 = pd.Series([1, 2, 3, 4, 5])
s3 = pd.Series([6, 7, 8, 9, 10])

s_soma = s2 + s3

print(f"{s_soma}\n")

#Exercício 3

s4 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(f"{s4[s4>5]}\n")

#Exercício 4

media = s1.mean()
std = s1.std()

print(f"{media}\n")
print(f"{std}\n")

#Exercicio 5

s_concat = pd.concat([s2, s3], axis = 1)
print(f"{s_concat}\n")

#Exercicio 6

s5 = pd.Series(range(10, 1, -1))

s_sub = s1 - s5
print(f"{s_sub}\n")

#Exercicio 7

s6 = pd.Series(range(1, 11))
s6.sort_values(ascending = False)

print(f"{s6}\n")

#Exercício 8

s7 = pd.Series(range(1, 11))

print(s7[3:8].min())
