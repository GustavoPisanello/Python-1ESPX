username = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
palavra_chave = input("Digite sua palavra-chave: ")
acertos = 0

if username == "Admin": 
    acertos += 1  
    if senha == "123456": 
        acertos += 1      
        if palavra_chave == "acessoADM":
            acertos += 1
            output = "Acesso concedido!"
        else:
            output = "Palavra-chave incorreta!"    
    else:
        output = "Senha Incorreta"
else:
        output = "Nome de usuário incorreto!"

erros = 3 - acertos

print(output)
if erros >= 2:
    print("Acesso bloqueado!!!")
