palavra_escolhida = input("Digite uma palavra a ser adivinhada: ")
palpite = input("Digite seu palpite: ")
chances = 3

if palavra_escolhida != palpite:
    chances -= 1
    print(f"Você errou! Você possui mais {chances} tentativas!")
    palpite = input("Digite o próximo palpite: ")

    if palavra_escolhida != palpite:
        chances-= 1
        print(f"Você errou! Você possui mais {chances} tentativa!")
        palpite = input("Digite o último palpite: ")

        if palavra_escolhida != palpite:
            chances -= 1
            print(f"Você perdeu! Não há mais chances! A palavra secreta era: {palavra_escolhida}")
    else:
        print(f"Parabéns! Você ganhou com {chances} tentativas!")
else:
    print("Parabéns! Você ganhou de primeira!")