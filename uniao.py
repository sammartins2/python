import forca
import adivinhacao

def escolhe_jogos():
    print()
    print("Bem vindo ao jogo de Adivinhação!")

    print("(1) forca (2) adivinhação")

    jogo = int(input("qual o jogo? "))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar()

    elif(jogo == 2):
        print("Jogando adivinhação")
        adivinhacao.jogar()

if(__name__=="__main__"):
    escolhe_jogos()