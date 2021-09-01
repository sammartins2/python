
def jogar():
    
    print()
    print("Bem vindo ao jogo da forca!")

    palavra_secreta = "ghiaccio".upper() #uper se usa para converter a a palavra minuscula em maiscula
    letras_acertadas = ["_" for letras in palavra_secreta]

    erros = 0
    print(len(palavra_secreta)) #len é para poder mostrar a quantidade ou tamanho
    print(letras_acertadas)


    while(True):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper() #strip serve para remover espaços em brancos tanto da direita quanto da esquerda

        if(chute in palavra_secreta):
            index = 0 
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1 
        else:
            erros += 1
            print("  _______     ")
            print(" |/      |    ")

            if(erros == 1):
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")

            if(erros == 2):
                print(" |      (_)   ")
                print(" |      \     ")
                print(" |            ")
                print(" |            ")

            if(erros == 3):
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")

            if(erros == 4):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")

            if(erros == 5):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")

            if(erros == 6):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")

            if (erros == 7):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

            print(" |            ")
            print("_|___         ")
            print()
        
        if (erros == 7):
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas) 

    if("_" not in letras_acertadas):
        print("Parabéns, você ganhou!")
        print("A palavra é {}".format(palavra_secreta))
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    print("Fim do jogo")
    print()

if(__name__=="__main__"):
    jogar()
