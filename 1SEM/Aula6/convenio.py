tempo_convenio = int(input("Digite o seu tempo de convênio, em meses: "))
permissao = bool

if tempo_convenio <= 6:
    print("Você tem acesso apenas à exames de sangue")
elif tempo_convenio < 12:
        print("Você tem acesso apenas à exames de sangue e radiografia")
elif tempo_convenio >= 12:
    convenio = input("Você tem acesso ao convênio? s/n: ")
    convenio = convenio.upper()
    if convenio == "S":
        permissao = True
    else:
        permissao = False
    print ("Acesso concedido" if permissao == True else "Acesso negado")
