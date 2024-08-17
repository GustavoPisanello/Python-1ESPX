def Fruits():
    fruits = ("maçã", "banana", "laranja", "uva");

    print(fruits[1]);

    fruits = list(fruits);

    mod_fruits = fruits.insert(2, "manga"); 

    mod_fruits = tuple(fruits);

    conc_fruits = mod_fruits + ("abacaxi", "limão");

    print(mod_fruits);

    for i in conc_fruits:
        if i == "uva":
            return True;

print(Fruits())
