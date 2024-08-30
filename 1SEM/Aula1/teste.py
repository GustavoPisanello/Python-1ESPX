avrg = []
def NumberOfGrades():
    """Selects the number of grades to be used in calculation
    
    Input:
    - The number of grades that will be used in the calculation of average
    """
    qty = int(input("Digite o número de notas que deseja realizar a média: "))
    InputGrades(qty)

def InputGrades(qty):
    """Inserts the grades istelf
    
    Input:
    - Grades (int)

    Parameters:
    - qty (quantity of grades - int)
    """
    i = 0
    while i < qty:
        grade = float(input(f"Digite a {i + 1}° Nota: "))
        i += 1
        if grade > 10:
            print("Não são permitidos números maiores que 10!")
            exit()
        else:
            avrg.append(grade)
    Average(qty)

def Average(qty):
    """Calculates the average grade based on the number of grades
    
    Output:
    - Result (The avarage itself - int)

    Parameter:
    - qty (quantity of grades - int)
    """
    result = round((sum(avrg)/qty), 1)
    Situation(result)

def Situation(result):
    """Informs the actual situation
    
    Parameter:
    - Result (The average itself - int)

    Output:
    - The user's situation
    """
    if result > 7:
        print(f"Sua nota é {result}! Você foi aprovado! :)")
    else: 
        print(f"Sua nota é {result}. Você foi reprovado :(")

if __name__ == "__main__":
    NumberOfGrades()