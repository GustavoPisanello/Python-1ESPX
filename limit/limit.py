import sympy

def Limit(): 
    x = sympy.symbols('x')
    equacao = input("Digite a equação: ")
    tendencia = input("Digite a tendência de x: ")

    # (Equação, variável, Tendência de X)
    limite = sympy.limit(equacao, x, tendencia) 
    print(limite)

if __name__ == "__main__":
    Limit()