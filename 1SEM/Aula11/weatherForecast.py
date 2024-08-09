# min/max/media/mediano

temperatures = []
def weatherForecast():
    while True:
        temp = int(input("Digite a temperatura: "))
        temperatures.append(temp)
        if temp == -999:
            break
    Calculum(temperatures)

def Calculum(x):
    x.sort()
    i = 0
    k = 0 

    while i < len(x):
        i += 1
    
    if len(temperatures) % 2 != 0:
        while k < (len(temperatures) / 2):
            k += 1
        
        print(f"Mediana: {temperatures[k - 1]}")
    else:
        print(f"A temperatura mediana é: {(temperatures[round(len(temperatures) / 2)] + temperatures[(round(len(temperatures) / 2)) - 1]) / 2}")

    print(f"A temperatura média é: {sum(x) / i}")
    print(f"A temperatura mínima é: {x[0]}")
    print(f"A temperatura máxima é: {x[i - 1]}")

weatherForecast()