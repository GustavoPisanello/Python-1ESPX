deadline = int(input("Digite o prazo de entrega: "))
status = input("Você é VIP? S/N: ")

if status == "S":
    vip = True
else:
    vip = False

if deadline <= 7:
    if vip == True:
        print("Seu pedido está sendo preparado para entrega expressa!")
    else:
        print("Seu pedido será entregue em breve")
elif 7 < deadline < 14:
    if vip == True:
        print("Seu pedido está em processo de embalagem especial")
    else:
        print("Seu pedido está sendo preparado")
else:
    print("Seu pedido está a caminho") 


