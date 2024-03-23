salario = float(input("Digite seu salário: "))

if salario < 2000:
    imposto = (salario * 0.1)
    salario_rest = salario - imposto
    print(f"O oposto será de: {imposto}")
    print(f"O seu salário líquido será de: {salario_rest}")

elif 2000 <= salario < 5000:
    imposto = (salario * 0.2)
    salario_rest = salario - imposto
    print(f"O oposto será de: {imposto}")
    print(f"O seu salário líquido será de: {salario_rest}")

elif 5000 <= salario < 10000:
    imposto = (salario * 0.24)
    salario_rest = salario - imposto
    print(f"O oposto será de: {imposto}")
    print(f"O seu salário líquido será de: {salario_rest}")

else:
    imposto = (salario * 0.30)
    salario_rest = salario - imposto
    print(f"O oposto será de: {imposto}")
    print(f"O seu salário líquido será de: {salario_rest}")