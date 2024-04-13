moeda_escolhida = input("Digite a moeda que deseja converter: ")
valor_desejado = float(input("Digite a quantidade de dinheiro: "))

if moeda_escolhida == "dólar":
    valor_real = valor_desejado * 5.12
    valor_iene = valor_desejado * 153.28
    valor_euro = valor_desejado * 0.94
    valor_dolar = 1
elif moeda_escolhida == "real":
    valor_dolar = valor_desejado * 0.20
    valor_iene = valor_desejado * 29.95
    valor_euro = valor_desejado * 0.18
    valor_real = 1
elif moeda_escolhida == "euro":
    valor_dolar = valor_desejado * 1.07
    valor_iene = valor_desejado * 163.57
    valor_real = valor_desejado * 5.46
    valor_euro = 1
else:
    valor_dolar = valor_desejado * 0.0065
    valor_euro = valor_desejado * 0.0061
    valor_real = valor_desejado * 0.033
    valor_iene = 1

print(f"Moeda escolhida: {moeda_escolhida} \n{moeda_escolhida} -> Dólar = {valor_dolar}\n{moeda_escolhida} -> Euro = {valor_euro}\n{moeda_escolhida} -> Iene = {valor_iene}\n{moeda_escolhida} -> Real = {valor_real}")
