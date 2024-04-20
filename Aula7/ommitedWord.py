text = input("Digite um texto: ").split(" ")
selectedWord = input("Digite uma palavra para quebrar no texto: ")
list = []

for i in text:
    if i == selectedWord:
        continue
    list.append(i)
    resposta = " ".join(list)
print(resposta)