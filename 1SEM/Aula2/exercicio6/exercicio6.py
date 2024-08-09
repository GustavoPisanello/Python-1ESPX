km = float(input("Digite a quantidade de quilômetros percorridos: "))
days = int(input("Digite a quantidade de dias em que o carro foi alugado: "))

ptp = 60 * days + km * 0.15

print(f"O valor total é de: {ptp}R$")