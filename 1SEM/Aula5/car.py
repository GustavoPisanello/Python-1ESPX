fab_year = int(input("Digite o ano de fabricação do carro: "))

if 2013 <= fab_year <= 2015:
    car_brand = input("Digite a marca do carro: ")
    car_brand = car_brand.title()
    if car_brand == "Volvo":
        print("A marca do carro é Volvo e foi fabricado entre os anos de 2013 e 2015")
    else:
        print("Carro fabricado entre os anos de 2013 e 2015, mas não é Volvo")
else:
    print("Seu carro está fora da faixa dos anos")