def calcular_media(lista):
  return sum(lista) / len(lista)

def solicitar_informacao():
  valores = []
  estado = True
  while estado:
    valor = input('Insira um número: ')
    valor = valor.lower()
    if(valor == 'fim'):
      estado = False
      break
    valores.append(float(valor))
  return valores

print(calcular_media(solicitar_informacao()))