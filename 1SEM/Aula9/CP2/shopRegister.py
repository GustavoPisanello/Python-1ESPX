produtos = []
i = 0
lista_produtos = ["notebook", "ssd", "mouse", "teclado", "monitor"]
contagem = 0

while i < 5:
    produto = input(f"Digite o {i + 1}° produto adquirido: ")
    produtos.append(produto)
    i += 1

for i in lista_produtos:
    contagem = 0
    for z in produtos:
        if z == i:
            contagem += 1
    print(f"Contagem de {i}: {contagem}")