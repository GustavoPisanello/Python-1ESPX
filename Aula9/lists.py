i = 0
pessoas = []

while i < 5:
    nome = input("Digite seu nome: ")
    cep = input("Digite seu cep: ")
    rg = input("Digite seu rg: ")

    pessoa = []

    pessoa.append(nome)
    pessoa.append(cep)
    pessoa.append(rg)

    pessoas.append(pessoa)

    i += 1

print(pessoas)