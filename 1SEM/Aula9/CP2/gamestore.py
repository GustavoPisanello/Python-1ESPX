itens_usu1 = []
itens_usu2 = []
k = 0
dados_usu1 = []
dados_usu2 = []

while k < 2:
    usuario_atual = []
    i = 0
    while i < 5:
        item = int(input(f"Usuário {k + 1}, Digite o valor do {i + 1}° item: "))
        usuario_atual.append(item)
        i += 1

    if k == 0:
        itens_usu1 = usuario_atual
    else:
        itens_usu2 = usuario_atual

    dados_atual = []

    soma = 0
    
    for i in usuario_atual:
        soma += i
    dados_atual.append(soma)
    media = soma / len(itens_usu1)
    dados_atual.append(media)
    
    if k == 0:
        dados_usu1 = dados_atual
    else:
        dados_usu2 = dados_atual

    k += 1

print(f"O valor total dos produtos do usuário 1 ficou em R${dados_usu1[0]}. Já a média ficou em R${dados_usu1[1]}")
print(f"O valor total dos produtos do usuário 2 ficou em R${dados_usu2[0]}. Já a média ficou em R${dados_usu2[1]}")