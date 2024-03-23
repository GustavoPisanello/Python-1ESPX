age = int(input("Digite sua idade: "))

if age < 15:
    print("Você não pode votar!")
    exit()
elif age >= 18:
    print("Obrigatório votar!")
else:
    titulo = input("Você possui título de eleitor? S/N ")
    titulo = titulo.upper()

    if titulo == "N":
        print("É seu direito")
    else:
        print("Você pode votar!")


    

