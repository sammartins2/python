print()

#Exercicio de exemplos 

idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade <= 12):
        print("Você é uma criança.")
    elif (idade >= 12):
        print("Você é um adolescente.")

print()

#mMostrar somente o numero

idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca     = idade < 12
adolescente = idade > 12

#Codifo modificado por mim mesmo, mas é o mesmo resultado do professor

print()

usuario = input("Informe o usuário do sistema! ")

nome = "Flavio" 

nome2 = "Douglas"

nome3 = "Nico"

if(usuario == nome):
    print("Seja bem-vindo Flavio!")
else:
    if(usuario == nome2):
         print("Seja bem-vindo Douglas")

    elif(usuario == nome3):
        print("Seja bem-vindo Nico")

    elif(usuario != nome, nome2, nome3): 
         print("Usuário não identificado!")

    
print()

#codigo do professor 


usuario = input("Informe o usuário do sistema!")

if(usuario == "Flavio"):
    print("Seja bem-vindo Flavio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")

print()

#Codigo feito por mim sozinho


numero_secreto = 23

chute_str = input("Digite um numero: ")

print("Você digitou ", chute_str)

chute = int(chute_str)

acertou = numero_secreto == chute

maior = chute >= numero_secreto 

menor = chute <= numero_secreto 

if(acertou):
    print("Parabens, você acertou !!!!!")

else:
    if(maior):
        print("Maior que o numero secreto ")
    elif(menor):
        print("Menor que o numero secreto")
print("FIM DE JOGO")