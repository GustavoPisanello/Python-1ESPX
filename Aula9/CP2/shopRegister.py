produtos = []
i = 0
lista_produtos = ["notebook", "ssd", "mouse", "teclado", "monitor"]
contagem = []

while i < 5:
    produto = input(f"Digite o {i + 1}° produto adquirido: ")
    produtos.append(produto)
    i += 1

for i in lista_produtos:
    for z in produtos:
        if z == i:
            contagem.append(i)
    
    if z in i:
        a = 0  
        while a < len(contagem):
            a += 1
        print(f"Contagem de {i}: {a}")

print(contagem)
