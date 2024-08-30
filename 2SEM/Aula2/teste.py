# Dia 16/08/2024 - Lista e tupla

lista = [100, 200, 300], [20, 40]

for i in lista:
    print(i)
 

tupla = (100, 200, 300), (3, 7)

for m in tupla:
    print(m) 

tupla = tuple(["foo", [1, 2, 3], True])
print(tupla)

tupla[1].append(4)
print(tupla) 
 
 #--------------------------

tupla = tuple(["foo", [1, 2, 3], True])

lista = list(tupla)
print(lista)

lista.insert(0, "fiap")
print(lista)

posicao_insercao = lista.index("foo") + 1
lista.insert(posicao_insercao, "foo fighters")

nova_tupla = tuple(lista)
print(nova_tupla) 

tupla = (4, None, "foo") + (4 , 5)
print(tupla) 

tupla =  (100, 1000, 10000)

a, b, c = tupla

print(a, b, c)

tupla54 = [5, 6, 7]
tupla53 = [4, 5, 7]

tuplaMestra = tupla54 + tupla53
print(tuplaMestra)