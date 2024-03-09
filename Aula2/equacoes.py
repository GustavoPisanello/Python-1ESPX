def Exhibition():
    op = int(input("""Escolha a equação: 

          1. 2x + 10
          2. 25x - 5
          3. 10x² + 2x + 10
          
          """))
    Choose(op)
    
def Choose(op):
    x = int(input("Digite o valor de x: "))
    match op: 
        case 1:
            print(Equation1(x))
        case 2:
            print(Equation2(x))
        case 3:
            print(Equation3(x))
        case _:
            print("Escolha um número válido")

def Equation1(x):
    print("Equação escolhida(1): 2x + 10 ")
    result = 2 * x + 10
    return (f"O resultado é: {result}")

def Equation2(x):
    print("Equação escolhida(2): 25x - 5")
    result = 25 * x - 5
    return (f"O resultado é: {result}")

def Equation3(x):
    print("Equação escolhida(3): 10x² + 2x + 10")
    result = 10 * x**2 + 2*x + 10
    return (f"O resultado é: {result}")
    
Exhibition()