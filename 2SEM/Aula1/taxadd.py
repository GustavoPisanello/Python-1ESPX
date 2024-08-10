def Input():
    gross_salary = float(input("Digite o salário bruto: "))
    
    tax = TaxCalculator(gross_salary)
    liquid_salary = gross_salary - (gross_salary * tax)
    print(f"""
        Salário bruto: R${str(round(gross_salary, 2)).replace(".", ",")}
        Salário líquido: R${str(round(liquid_salary, 2)).replace(".", ",")}
        Taxa aplicada: R${str(round(tax*100, 1)).replace(".", ",")}%
    """)

def TaxCalculator(x):
    if x < 2112:
        print(f"Você é isento de imposto de renda! Seu salário continua em R${x}")
        exit()
    elif x < 2826.66:
        tax = 0.075
    elif x < 3751.06:
        tax = 0.15
    elif x < 4664.68:
        tax = 0.225
    else:
        tax = 0.275
    return tax

if __name__ == "__main__":
    Input()
