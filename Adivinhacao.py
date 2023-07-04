# O jogo, so que com FOR
import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("O seu chute foi maior que o número secreto")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

'''
import random
print("*****************")
print("Adivinhe o numero")
print("*****************")

numero_secreto = random.randrange(1, 101)
tentativas = 0
rodada = 1
pontos = 1000


print("Qual a dificuldade escolhida para o jogo?")
print("(1) Facíl (2) Médio (3) Dificil")

dificuldade = int(input("Qual o nivel de dificuldade escolhida: "))

if(dificuldade == 1):
    tentativas = 20
elif(dificuldade == 2):
    tentativas = 15
else:
    tentativas = 10

while(rodada <= tentativas):
    print("Voce esta na rodada {} de {}".format(rodada , tentativas ))
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print("Coloque um número de 1 a 100")
        continue


    correto = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if (correto):
        print("Acertou e fez {} pontos".format(pontos))
        break
    else:
        if(maior):
            print("O seu chute foi maior do que o número secreto!")
        elif(menor):
            print("O seu chute foi menor do que o número secreto!")
        pontos_perdidos = abs(chute - numero_secreto)   #pontos perdidos da rodada
        pontos = pontos - pontos_perdidos               #subtraindo os pontos perdidos da pontuação total 
        rodada = rodada + 1
print("O numero era: ", numero_secreto)

print("*****************")
print("*  FIM DO JOGO  *")
print("*****************")

'''