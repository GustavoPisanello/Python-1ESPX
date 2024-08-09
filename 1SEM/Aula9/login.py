chances = 3

for i in range(chances):
    emailUsu = input("Digite seu email: ")
    senhaUsu = input("Digite sua senha: ")

    emailCorreto = "adm@gmail.com"
    senhaCorreta = "123456"
    
    if emailUsu != emailCorreto or senhaUsu != senhaCorreta:
        chances -= 1
        if chances != 0:
            print(f"Você errou! Restam apenas {chances} tentativa(s)!")
        else:
            print("Limites de tentativas excedidos! Login bloqueado temporariamente.")
    else:
        print("Acesso concedido")
        break
    