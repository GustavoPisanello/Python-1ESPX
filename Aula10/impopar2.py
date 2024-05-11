def Impopar():
    """Defines if the number is odd or even
    Input:
    - The number itself (x - int)
    """
    x = int(input("Digite um número: "))

    result = x % 2

    if result == 1:
        return f"O número {x} é ímpar"
    else:
        return f"O número {x} é par"

print(Impopar())
