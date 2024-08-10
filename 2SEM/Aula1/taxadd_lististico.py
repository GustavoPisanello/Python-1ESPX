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
    tax_list = [(2112, 0), (2826.66,0.075), (3751.06, 0.15), (4664.68, 0.225), (float('inf'), 0.275)]

    for i, z in tax_list:
        if x <= i:
            return z

if __name__ == "__main__":
    Input()