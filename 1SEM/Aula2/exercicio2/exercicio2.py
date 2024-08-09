days = int(input("Digite a quantidade de dias: "))
hours = int(input("Digite a quantidade de horas: "))
minutes = int(input("Digite a quantidade de minutos: "))
seconds = int(input("Digite a quantidade de segundos: "))

dis = days * 24 * 60 * 60
his = hours * 60 * 60
mis = minutes * 60

result = dis + his + mis + seconds

print(result)