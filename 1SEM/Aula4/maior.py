num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")
num3 = input("Digite outro número: ")

if num1 == num2 > num3:
    print("Os números 1 e 2 são os maiores!")
elif num2 == num3 > num1:
    print("Os números 2 e 3 são os maiores!")
elif num1 == num3 > num2:
    print("Os números 1 e 3 são os maiores!")
elif num1 > num2 and num3:
    print("O primeiro número é o maior!")
elif num2 > num1 and num3:
    print("O segundo número é o maior!")
else:
    print("O terceiro número é o maior!")