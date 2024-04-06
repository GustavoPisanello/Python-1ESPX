hour = int(input("Digite a hora: "))
temperature = int(input("Digite a temperatura: "))

if 6 <= hour <= 12:
    if temperature > 20:
        print("Hora de fazer uma caminhada no parque")
    else:
        print("Hora de tomar um café da manhã")
elif 12 < hour < 18:
    if temperature > 25:
        print("Que tal um piquenique")
    else: print("Hora de almoçar")
else:
    print("Hora de relaxar em casa")