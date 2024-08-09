age = int(input("Digite sua idade: "))

if age <= 12:
    print("Você é uma criança!")
elif age < 18:
    print("Você é um adolescente!")
elif age > 60:
    print("Você é um idoso!")
else: 
    print("Você é um adulto!")