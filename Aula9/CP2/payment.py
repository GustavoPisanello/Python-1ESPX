lista_salarios = [1800, 2500, 3200, 4200, 5000]
salario_10 = []
salario_20 = []
salario_30 = []

for i in lista_salarios:
    if i < 0:
        print("Seu salário não pode ser negativo! Denuncie!")
    else:
        if i  < 2000:
            desconto = 0.1
            salario_liquido = i - (i * desconto)
            salario_10.append(salario_liquido)
        elif i < 4000:
            desconto = 0.2
            salario_liquido = i - (i * desconto)
            salario_20.append(salario_liquido)
        else:
            desconto = 0.3
            salario_liquido = i - (i * desconto)
            salario_30.append(salario_liquido)
    
print(f"Salários menores que R$2.000: \n {salario_10} | Desconto de 10%")
print(f"Salários entre R$ 2.000 e R$4.000: \n {salario_20} | Desconto de 20%")
print(f"Salários maiores que R$4.000: \n {salario_30} | Desconto de 30%")
        