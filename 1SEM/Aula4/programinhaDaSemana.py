weekday = input("Digite o dia: ")
weekday = weekday.title()

if weekday == "Sábado":
    print("Dia de balada")
elif weekday == "Domingo":
    print("Dia de Netflix, Futebol ou Cinema")
else:
    print("Dia de trabalhar ou estudar :(")
