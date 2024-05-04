i = 0
qty = 5
soma = 0

while i < qty:
    num = int(input(f"Digite o {i + 1}° número: "))
    soma += num
    i += 1

media = soma/qty

print(media)