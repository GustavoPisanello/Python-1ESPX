""" str = "Teste de string"

print(str[9:] + " legal")
 """
name = input("Digite seu nome: ")

age = int(input("Digite sua idade: "))

city = input("Digite sua cidade: ")

ano = "anos"
if age == 1:
    ano = "ano"

msg = f"Meu nome é {name}, tenho {age} {ano} e moro na cidade de {city}"
print(msg)
