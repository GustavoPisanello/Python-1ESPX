vel = int(input("Digite a velocidade do carro: "))
valorExcedido = (vel - 80)
multa = (valorExcedido)* 5

print(f"Você excedeu a velocidade máxima em {valorExcedido}Km/h! Sua multa ficou em R${multa}")