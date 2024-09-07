import statistics

lista1 = [10, 20, 30, 40, 50]
lista2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
lista3 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

def Soma(x):
    soma = sum(x)
    return soma

def Media(x):
    media = statistics.mean(x)
    return media

soma1 = Media(lista1)
soma2 = Media(lista2)
soma3 = Media(lista3)

media1 = Media(lista1)
media2 = Media(lista2)
media3 = Media(lista3)

print(f"Soma das lista 1: {soma1}\nSoma da lista 2: {soma2}\nSoma da lista 3: {soma3}")
print(f"Média das lista 1: {media1}\nMédia da lista 2: {media2}\nMédia da lista 3: {media3}")

print(f"Soma das somas das listas: {soma1 + soma2 + soma3}")
print(f"Média das médias das listas: {(media1 +  media2 + media3)/ 3}")

