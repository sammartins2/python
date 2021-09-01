
import random

def jogar():

    print()
    print("Bem vindo ao jogo de Adivinhação!")

    numero_secreto = random.randrange(1,11)#gerar numeros aleatorios de 1 a 10 ou o tanto que a pessoa quiser print(")
    tentativas = 0
    pontos = 10

    print("Qual nível de dificuldade ??")
    print("(1) fácil 5 tentativas (2) Médio 3 tentavivas (3) Difícil 1 tentativa")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        tentativas = 5

    elif(nivel == 2):
        tentativas = 3

    else:
        tentativas = 1    

    while (tentativas > 0):
        print("tentativas", tentativas)
        chute_str = input("Digite um numero entre 1 e 10: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 10):
            print("Você deve digitar um numero entre 1 a 10!")
            continue

        acertou = numero_secreto == chute

        chute_maior = chute > numero_secreto

        chute_menor = chute < numero_secreto

        if (acertou):
            print("Você acertou Você fez {} pontos !".format(pontos))
            break
        else:
            if(chute_maior):
                print("Você errou! O seu chute foi maior do que o numero secreto")
            
            elif(chute_menor):
                print("Você errou! O seu chute foi menor do que o numero secreto")

        tentativas = tentativas - 1
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("Fim do jogo")
    print()

if(__name__=="__main__"): 
    jogar()

