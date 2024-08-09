colors = ["Azul", "Verde", "Amarelo"]

def VerifyColors(color):
    color = color.title()
    for i in colors:
        if i == color:
            print(f"A cor {color} está presente na lista")
            break
        else:
            print(f"A cor {color} NÃO está presente na lista")
            break

color = input("Digite a cor: ")
VerifyColors(color)