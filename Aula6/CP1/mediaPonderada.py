valor1 = float(input("Digite o primeiro valor de venda: "))
peso1 = float(input("Digite o peso do primeiro valor de venda: "))
valor2 = float(input("Digite o segundo valor de venda: "))
peso2 = float(input("Digite o peso do segundo valor de venda: "))
valor3 = float(input("Digite o terceiro valor de venda: "))
peso3 = float(input("Digite o peso do terceiro valor de venda: "))
valor4 = float(input("Digite o quarto valor de venda: "))
peso4 = float(input("Digite o peso do quarto valor de venda: "))

media_ponderada = ((valor1 * peso1 ) + (valor2 * peso2) + (valor3 * peso3) + (valor4 * peso4))/ (peso1 + peso2 + peso3 + peso4)
media_ponderada = round(media_ponderada)

valor1_porcento = (valor1/media_ponderada)
valor2_porcento = (valor2/media_ponderada)
valor3_porcento = (valor3/media_ponderada)
valor4_porcento = (valor4/media_ponderada)

print(f"Porcentagem venda 1 = {round(valor1_porcento * 100)}%")
print(f"Porcentagem venda 2 = {round(valor2_porcento * 100)}%")
print(f"Porcentagem venda 3 = {round(valor3_porcento * 100)}%")
print(f"Porcentagem venda 4 = {round(valor4_porcento * 100)}%")