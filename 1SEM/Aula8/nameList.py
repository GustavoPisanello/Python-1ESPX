qty = int(input("Digite a quantidade de nomes que deseja inserir: "))
i = 0
nameList = []

while i < qty:
    name = input(f"Digite o {i + 1}° nome: ")
    nameList.append(name)
    i += 1

print(nameList)
