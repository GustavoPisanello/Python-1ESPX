nome = input("Digite seu nome: ")
nacionalidade = input("Digite sua nacionalidade: ")

if nacionalidade == "alemao":
    print(f"Boas vindas ao Brasil, {nome}! Você é Alemão e, portanto, preciso do número do seu passaporte.")
    numPassaporte = input("Digite o número do seu passaporte: ")
    print("Tudo certo. Obrigado pela visita!")
elif nacionalidade == "britânico":
    print(f"Boas vindas ao Brasil, {nome}! Você é Britânico e, portanto, preciso do número do seu passaporte.")
    numPassaporte = input("Digite o número do seu passaporte: ")
    print("Tudo certo. Obrigado pela visita!")
else:
    print("Bem vindo de volta! Você é Brasileiro, então não preciso do número do seu passaporte. Tenha um bom dia!")
