def Payment(qtygrossSalaries):
    """Calculates the liquid salary, based on the gross value
    
    Paramater:
    - The quantity of salaries that will be calculated (qtygrossSalaries)

    Return:
    - The net salary (netSalary)
    """
    i = 0
    grossSalaries =[]
    netSalaries = []

    while i < qtygrossSalaries:
        payment = int(input(f"Digite o {i + 1}° salário: "))
        grossSalaries.append(payment)
        i +=1
    
    for k in grossSalaries:
        discount = Discount(k)
        grossSalary = k - (k * discount)
        netSalaries.append(grossSalary)

    return netSalaries

def Discount(x):
    """Calculates the respective salary discount, based on its value
    
    Parameters:
    - The salaries list (x)

    Return:
    - The discount value (discount)
    """
    if x < 1400:
        discount = 0
    elif x < 2999:
        discount = 0.1
    elif x < 3999:
        discount = 0.2
    else: 
        discount = 0.3
    
    return discount

numSalaries = int(input("Digite a quantidade de salários que deseja realizar o cálculo de desconto: "))
print(Payment(numSalaries))