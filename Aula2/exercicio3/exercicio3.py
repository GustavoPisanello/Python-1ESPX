price = float(input("Digite o preço do produto: "))
discount = float(input("Digite o desconto aplicado: "))
total = price - (price * (discount/100))

print(f"O preço com desconto é: {total}")