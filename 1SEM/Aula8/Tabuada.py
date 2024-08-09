num = int(input("Digite um número para a tabuada: "))
multList = []

for i in range(1,11):
    result = num * i
    multList.append(result)

print(multList)