artigo = input("Você possui um artigo publicado? S/N ")
artigo = artigo.upper()

if artigo == "S":
    print("Aprovado!")
    exit()

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

result = ((nota1 + nota2 + nota3)/3)

if result >= 7:
    print("Aprovado!")
elif result < 4: 
    print("Reprovado!")
else: 
    print("Exame!")
