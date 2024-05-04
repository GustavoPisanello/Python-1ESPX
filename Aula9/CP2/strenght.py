velLuz = 300000
forca = [500, 1000, 1500, 2000, 2500, 3000]
massas =[]

for i in forca:
    massa = i / velLuz
    massas.append(massa)

print(f"{massas}")


