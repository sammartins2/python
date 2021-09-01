print()
print("Bem vindo novamente")
print()

numero_secreto = 23
total_de_tentavivas = 2
rodada = 1

while(rodada <= total_de_tentavivas):
    print("Tentativa", rodada, "de", total_de_tentavivas)
    chute = int (input("Digite o seu numero: ")) #input cria uma entrada e lê a função digitada. int serve para converter uma string para int

    print("voce digitou " , chute)

    if(numero_secreto == (chute)): 
        print("Você acertou, o numero era: ", numero_secreto)
    else:
        if (chute > numero_secreto):
            print("voce errou! chute maior que o numero secreto")
        elif (chute < numero_secreto):
            print("Você errou! chute menor que o numero secreto")
    
    rodada = rodada + 1
        

print("fim do jogo")