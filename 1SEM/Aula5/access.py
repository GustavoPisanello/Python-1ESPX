username = input("Digite o nome de usuário: ")
pswd = input("Digite sua senha: ")
security_word = input("Digite sua palavra de sgurança: ")

if username == "Admin":
    if pswd == "Senha123":
        if security_word == "Betoneira":
            print("Seja muito bem-vindo, ó grande senhor Adeemi")
        else:
            print("Você errou a palavra de segurança! | Dica: Tem a ver com contrução civil ;)")
    else:
        print("Você errou a senha | Dica: A melhor senha existente ;)")
else:
    print("Você errou o nome de usuário! Tente novamente! | Dica: Admininastro ;)")
    