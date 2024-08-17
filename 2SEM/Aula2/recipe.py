def Muquiranas():
    pessoas = ["Paulo", "José", "Ana", "Pedro"];
    despesas =[(5000, 15000, 25000, 9800),
                (230, 100, 50, 415),
                (50, 15, 89, 115)];

    despesas_viagem = despesas[0];
    despesas_rest = despesas[1];
    despesas_transp = despesas[2];

    despesas_totais_list = []
    despesa_dono = []
    z = 0
    for i in pessoas:
        despesas_totais = despesas_viagem[z] + despesas_rest[z] + despesas_transp[z];   
        despesas_totais_list.append(despesas_totais)
        z += 1
        print(f"O(A) viajante {i} gastou {despesas_totais}")
        despesas_totais = str(despesas_totais)
        despesa_dono.insert(z, f"{i} {despesas_totais}")

    despesas_totais_list.sort()
    
    print(f"O mais muquirana foi: {despesas_totais_list[0]}, e o mais gastão foi: {despesas_totais_list[z - 1]}")
    print(despesa_dono)
    
Muquiranas()