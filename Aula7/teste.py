palavra = "Hoje é dia de Happy Hour"

""" for k in palavra:
    if k == "a":
        break
    print(k) """

    
for k in palavra:
    if k == "a" or k == "e" or k == "i" or k == "o" or k == "u":
        continue
    print(k)