def Input():
    values = []
    for i in range(0,5):
        value = int(input("Digite um valor: "))
        values.append(value)
    return media(values)

def media(x):
    soma = 0
    for i in x:
        soma += i
        
    media = soma / len(x)
    return media

print(Input())