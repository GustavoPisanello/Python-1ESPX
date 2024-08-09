list2 =[]

for i in range(0, 2):
    name = input("Digite seu nome: ")
    age = input("Digite sua idade: ")
    cpf = input("Digite seu CPF: ")
    rg = input("Digite seu RG: ")

    list = [{"Nome": name, "Idade": age, "CPF": cpf, "RG": rg}]
    list2.append(list)
    
for i in range(0,2):
    print(f"{list2[i]}")


