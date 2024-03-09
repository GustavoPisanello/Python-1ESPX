op = int(input(""" --- Cálculo de Potência ---
           
           Deseja inserir:
           
            1. Tensão(V) e Corrente
            2. Resistência(R) e Corrente(I)
            3. Tensão(V) e resistência(R)
           
           """))

if op == 1:
    v = int(input("Digite o valor da Tesão: "))
    i = int(input("Digite o valor da Corrente: "))
    p = v * i
    print(f"O valor da potência é de: {p}")

elif op == 2:
    i = int(input("Digite o valor da Corrente: "))
    r = int(input("Digite o valor da Resistência: "))
    p = r * i* i
    print(f"O valor da potência é de: {p}")
else:
    r = int(input("Digite o valor da Resistência: "))
    v = int(input("Digite o valor da Tesão: "))
    p = v * v / r
    print(f"O valor da potência é de: {p}")

