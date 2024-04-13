produto1 = int(input("Digite a quantidade do produto 1: "))
valor1 = int(input("Digite o valor do produto 1: "))
produto2 = int(input("Digite a quantidade do produto 2: "))
valor2 = int(input("Digite o valor do produto 2: "))
produto3 = int(input("Digite a quantidade do produto 3: "))
valor3 = int(input("Digite o valor do produto 3: "))
produto4 = int(input("Digite a quantidade do produto 4: "))
valor4 = int(input("Digite o valor do produto 4: "))

result1 = produto1 * valor1
result2 = produto2 * valor2
result3 = produto3 * valor3
result4 = produto4 * valor4

if result1 > result2 > result3 > result4:
    print(f"Produto 1: {result1} \nProduto 2: {result2} \nProduto 3: {result3} \nProduto 4: {result4}") 
elif result1 > result3 > result2 > result4:
    print(f"Produto 1: {result1} \nProduto 2: {result3} \nProduto 3: {result2} \nProduto 4: {result4}") 
elif result1 > result3 > result4 > result2:
    print(f"Produto 1: {result1} \nProduto 2: {result3} \nProduto 3: {result2} \nProduto 4: {result4}") 