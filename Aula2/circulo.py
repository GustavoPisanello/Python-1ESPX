import math

def VerifyValue(radius):
    if radius < 0:
        print("Digite um número positivo!")
        exit()
    return radius

def main():
    radius = float(input("Digite o raio do círculo: "))
    VerifyValue(radius)
    area = math.pi * (radius ** 2)
    print(f"A área do círculo é: {area}")

if __name__ == "__main__":
    main()