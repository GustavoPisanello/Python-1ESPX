import os

x = int(input("Digite sua opção: \n 1. Fahrenheit para Celsius \n 2. Celsius para Fahrenheit: \n"))

def Choose(x):
    match x:
        case 1:
            FtoC()
        case 2:
            CtoF()
        case _:
            os.system("cls")
            print("Digite uma opção válida!")
            Choose(x)
        
def FtoC():
    while True:
        temp_f = float(input("Insira um valor de temperatura: "))
        temp_c = (9/5) * (temp_f - 32)
        print(f"{temp_f}°F - {round(temp_c, 2)}°C")
        if temp_f == 0:
            break

def CtoF():
    while True:
        temp_c = float(input("Insira uma temperatura em Celsius: "))
        temp_f = (temp_c * (9/5)) + 32
        print(f"{temp_c}°C - {round(temp_f, 2)}°F")
        if temp_c == 0:
            break

Choose(x)

    