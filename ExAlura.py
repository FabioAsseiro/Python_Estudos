print("*****************")
print("Adivinhe o numero")
print("*****************")

import random
numero_secreto = random.randint(0, 100)
tentativas = 5
rodada = 1

while(rodada <= tentativas):
    print("Voce esta na rodada {} de {}".format(rodada , tentativas ))
    chute_str = input("Digite um numero: ")
    chute = int(chute_str)

    correto = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if (correto):
        print("Acertou!")
        tentativas = 0
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")

        rodada = rodada + 1



print("O numero era: ", numero_secreto)

print("*****************")
print("*  FIM DO JOGO  *")
print("*****************")
