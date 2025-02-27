#JOGO DE ADIVINHAÇÃO
#DESENVOLVIDO POR PIETRO SOUZA
import random
#Gerando um numero aleatório
numero_aleatorio = random.randint(1,10)

pergunta = int(input("chuta um numero de 1 a 10 "))
if pergunta == numero_aleatorio:
    print (f"parabens voçe acertou o numero é {numero_aleatorio}")
else:
    print ("voçe errou melhorar")