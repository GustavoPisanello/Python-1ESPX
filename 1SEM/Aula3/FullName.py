fullname = input("Digite seu nome: ")

separe = (fullname.split(" "))
len = len(separe)

i = 0
upperFullName = []

while i < len:

    firstLetter = (separe[i][0])
    maiusculo = firstLetter.upper()
    upperName = f"{maiusculo}{separe[i][1:].lower()}"
    upperFullName.append(upperName)
    i += 1

cpf = input("Digite seu CPF: ")

formatCPF = (f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}")

city = input("Digite sua cidade: ")

print(f"{' '.join(upperFullName)}, Seu CPF é: {formatCPF}, Sua cidade é: {city.title()}")


