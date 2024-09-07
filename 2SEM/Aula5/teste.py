import statistics
def SomaSub(a,b,c):
    "Função que soma 3 números"
    somar = a + b + c
    sub = a - b - c
    return somar, sub

soma, subtracao = SomaSub(1,2,3)
print(soma)
print(subtracao)