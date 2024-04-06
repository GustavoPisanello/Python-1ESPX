age = int(input("Digite sua idade: "))
total_purchase = float(input("Insira o valor da sua compra: "))

if age >= 65:
    if total_purchase >= 100:
        print("Você terá 10% de desconto")
    else:
        print("Você não terá direito ao desconto")
else:
    print("Você está fora da faixa etária para ter o desconto")