def Calculo(w, x, y, z):
    soma = w + x + y + z
    sub = w - x - y - z
    mult = w * x * y * z
    div = w / x / y / z

    return soma, sub, mult, div

soma, sub, mult, div = Calculo(1, 2, 3, 4)

print(soma)
print(sub)
print(mult)
print(div)
