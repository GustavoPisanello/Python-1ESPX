# Nome do time / Pontos / Vitórias / Derrotas

print("\n")

dados = (
("Fortaleza", 48, 14, 3),
("Botafogo", 47, 14, 5),
("Palmeiras", 44, 14, 5),
("Flamengo", 44, 13, 5),
("São Paulo", 41, 12, 5)
)

taxas_pontos_vitoria = []
taxas_pontos_derrota = []

for w, x, y, z in dados:
    taxa_pontos_vitoria = (x / (x + y)), w
    taxas_pontos_vitoria.append(taxa_pontos_vitoria)
   
    taxa_pontos_derrota = (x / (x + z)), w
    taxas_pontos_derrota.append(taxa_pontos_derrota)
   
    print(f"O {w} teve uma taxa de pontos/vitória de: {taxa_pontos_vitoria[0]}, e uma taxa de pontos/derrota de: {taxa_pontos_derrota[0]}")

taxas_pontos_vitoria.sort(reverse=True)
taxas_pontos_derrota.sort(reverse=True)

print(f"\nO time com maior taxa de pontos/vitória foi o {taxas_pontos_vitoria[0][1]}, com a taxa de {taxas_pontos_vitoria[0][0]}")
print(f"O time com menor taxa de pontos/vitória foi o {taxas_pontos_vitoria[len(taxas_pontos_vitoria) - 1][1]}, com a taxa de {taxas_pontos_vitoria[len(taxas_pontos_vitoria) - 1][0]}")

print(f"\nO time com maior taxa de pontos/derrota foi o {taxas_pontos_derrota[0][1]}, com a taxa de {taxas_pontos_derrota[0][0]}")
print(f"O time com menor taxa de pontos/derrota foi o {taxas_pontos_derrota[len(taxas_pontos_derrota) - 1][1]}, com a taxa de {taxas_pontos_derrota[len(taxas_pontos_vitoria) - 1][0]}")





dados = list(dados)
dado_adicional = ("Fluminense", 24, 6, 6)
dados.append(dado_adicional)
dado_adicional = ("Vitória", 22, 6, 4)
dados.append(dado_adicional)
dado_adicional = ("Corinthians", 22, 4, 10)
dados.append(dado_adicional)
dado_adicional = ("Cuiabá", 18, 4, 6)
dados.append(dado_adicional)
dado_adicional = ("Atlético-GO", 18, 4, 6)
dados.append(dado_adicional)
dados = tuple(dados)
""" 
def Concatena(dados, m, n, o, p):
dados = list(dados)
dado_adicional = (m, n, o, p)
dados.append(dado_adicional)
dados = tuple(dados)
return dados """


dados = list(dados)
posicao_insercao = dados.index(('Fluminense', 24, 6, 6))
dados.insert(posicao_insercao, ("Fluminense", 28, 7, 7))
dados.remove(('Fluminense', 24, 6, 6))

dados = tuple(dados)
print(dados)

soma_pontos = 0
soma_vitorias = 0
soma_derrotas = 0

for f in dados:
    soma_pontos += f[1]
    soma_vitorias += f[2]
    soma_derrotas += f[3]

print(soma_pontos)
print(soma_vitorias)
print(soma_derrotas)
