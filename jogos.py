import Forca
import Adivinhacao

print("***************************")
print("Bem vindo, escolha um jogo!")
print("***************************")



print("(1) Adivinhação (2) Forca")

jogo = int(input("Qual jogo você vai jogar?"))

if(jogo == 1):
    print("Você ira jogar Adivinhação")
    Adivinhacao.jogar()
elif(jogo == 2):
    print("Você ira jogar Forca")
    Forca.jogar()
else:
    print("Codigo errado, tente novamente!")
    