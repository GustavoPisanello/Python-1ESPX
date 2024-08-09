phrase = input("Digite uma frase: ")
contagem = 0
i = 0

while i < len(phrase):
    if phrase[i] == "a":
        contagem += 1
    i += 1
print(f'A letra "A" aparece {contagem} vezes')