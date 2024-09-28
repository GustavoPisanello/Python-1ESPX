inputs = []


i = 0
while i < 2:
    cidade = []
    for z in range(0, 2):
        temp = int(input(f"Digite a {i + 1}° temperatura: "))
        cidade.append(temp)
    inputs.append(cidade)
    i+= 1

def mediaGlobal(x):
    somaTemp = 0
    for i in x:
        for z in i:
            somaTemp += z
    
    mediaTemp = somaTemp / (len(x) * len(x[0]))

    return mediaTemp

mediasInd = []

def medias(x):
    somar = somas(x);
    somasInd = []
    soma = 0
    for i in somar:
        soma += i
        somasInd.append(soma)
    soma = 0
    
    medias = []
    media = 0
    for z in somasInd:
        media = z / len(somasInd)
        medias.append(media)

    return medias

def somas(x):
    somas = []
    for i in x:
        somar = sum(i)
        somas.append(somar)

    print(somas)
    return somas


print(medias(inputs))