import statistics

lista = [10, 20, 30, 40, 50]

def Calculo(x):
    soma = sum(x)
    media = statistics.mean(x)

    return soma, media

soma, media = Calculo(lista)

print(soma)
print(media)