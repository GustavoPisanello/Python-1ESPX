import math

""" def Square(x):
    y = x**2
    return y

def SquareSum(x, y):
    squareSum = Square(x) + Square(y)
    return squareSum

print(SquareSum(3, 6)) """

""" def Area(w, h):
    area = w * h
    return area

def ShowArea():
    x = int(input("Digite o comprimento: "))
    y = int(input("Digite a largura: "))
    
    print(f"A área do retângulo é: {Area(x, y)}")

ShowArea() """

def CircleArea(r):
    circleArea = math.pi * r ** 2

    if circleArea > 100:
        circleSize = "grande área"
    elif circleArea > 50:
        circleSize = "área média"
    else:
        circleSize = "pequena Área"

    return circleArea, circleSize

def InputAndPrint():
    r = float(input("Digite o raio do círculo: "))
    x, y = CircleArea(r)

    print(f"A área do círculo é de aproximadamente: {round(x, 2)}. O círculo tem uma {y}")

InputAndPrint()
