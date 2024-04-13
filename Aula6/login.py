email = input("Digite o email: ")

if email == "administrador@gmail.com":
    password = input("Digite a senha: ")
    if password == "123456":
        security_code = input("Digite o código de segurança")
        if security_code == "123":           
            print("Acesso Concedido!")
        else:
            print("Código de segurança inválido")
    else: 
        print("Senha inválida")
else:
    print("Email inválido!")