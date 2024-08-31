# Exercício 1 - mídias digitais

# Mídia digital, likes, dislikes

dados = (('youtube', 550, 10),
('facebook', 882, 50),
('linkedin', 1226, 5),
('instagram', 550000, 65))

soma_likes = 0
soma_dislikes = 0

for z in dados:
    soma_likes += z[1]
    soma_dislikes += z[2]

media_likes = (soma_likes / len(dados))
media_dislikes = (soma_dislikes / 4)


ordenacao = []
i = 0
while i < len(dados):
    ordenado = dados[i][1:]
    ordenacao += ordenado
    i += 1

ordenacao.sort()
ordenacao = tuple(ordenacao)

taxas_juntas = []

for w, y, x in dados:
    taxa_likes = y / (y + x)
    taxas_juntas.append(taxa_likes)
    print(f"Taxa de likes do {w}: {taxa_likes}")

taxas_juntas.sort()

print(soma_likes)
print(soma_dislikes)
print(media_likes)
print(media_dislikes)

print(ordenacao)
print(taxas_juntas)

print(f"Menor taxa: {taxas_juntas[0]}")
print(f"Maior taxa: {taxas_juntas[len(taxas_juntas) - 1 :]}")

