payment = float(input("Digite seu salário: "))
anual_payment = (payment * 12)

if payment <= 1412:
    aliquot = 0.075
elif payment < 2666.68:
    aliquot = 0.09
elif payment < 4000.03:
    aliquot = 0.12
elif payment < 7786.02:
    aliquot = 0.14
else: 
    aliquot = 0.275

tax = anual_payment * aliquot

tax = round(tax, 2)
print(f"O imposto de renda referente ao seu salário é de: {tax}")