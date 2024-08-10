def Input():
    i = 1
    k = 1
    notas = []
    medias = 0

    while i < 4:
        while k < 4:
            nota = float(input(f"Digite a {k}° nota do {i}° Aluno: "))

            if nota < 0 or nota > 10:
                print("As notas permitidas vão de 0-10. Revise sua entrada")
                continue

            notas.append(nota)
            k+=1

        print(f"A média do {i}° aluno é: {round(Mediador(notas), 2)}")
        medias += Mediador(notas)
        
        i+=1
        k=1

    media_global = medias / (i - 1)
    print(f"A média global é: {round(media_global, 2)}")

def Mediador(lista):
    soma = 0
    media = 0
    for z in lista:
        soma += z
    media = soma/len(lista)
    return media

if __name__ == "__main__":
    Input()