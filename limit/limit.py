import sympy

# Import obrigatório para usar as funções da bilbioteca sympy.
# Necessário baixar a biblioteca. Para isso, use o comando "pip install sympy" no terminal.
# Se estiver usando o terminal, utilize o comando "python limit.py" para rodar o programa.

# Note que, ao usar potência, é necessário usar dois asteriscos em sequência e sem espaço entre eles: "**".
# Note também a importância de multiplicar a variável 'x' com o termo que a acompanha. Este programa não identifica números como '5x'. Para escrever isso corretamente no input, é necessário escrever '5*x' -> 'Cinco vezes xis'.
# Se quiser usar o conceito de 'infinito' ou 'infinito negativo', use dois o's minúsculos em sequência: "oo" e "-oo", respectivamente.

def Limit(): 
    """ Calcula o limite da função digitada com base na tendência da variável 'x'. 
        - Exemplo de Input: \n 
            Equação: ((x**2 - 9) / (x - 3))
            Tendência de x: 3

        - Output esperado: 6

    """
    x = sympy.symbols('x')
    equacao = input("\nDigite a equação: ")
    tendencia = input("Digite a tendência de x: ")

    # (Equação, variável, Tendência de X)
    limite = sympy.limit(equacao, x, tendencia) 
    print(f"\nQuando 'X' tende à {tendencia}, O limite da função é: {limite}\n")

if __name__ == "__main__":
    Limit()