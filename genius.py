import winsound
import time 
import random

lista_frequencias = [300,600,1200,2400]

lista_sequencia = []

print("Seja bem vindo!")

print("Preste atenção nas frequências")
input("(Pressione ENTER para continuar)")


indice = 0
for frequencia in lista_frequencias:
    print(indice)
    winsound.Beep(frequencia,500)
    time.sleep(0.6)
    indice = indice + 1

time.sleep(0.5)

print("Prepare-se para o jogo:")

while True:
    print("Preste atenção na sequencia")
    time.sleep(1)

    som_escolhido = random.choice(lista_frequencias)

    lista_sequencia.append(som_escolhido)

    for frequencia in lista_sequencia:
        winsound.Beep(frequencia, 500)
        time.sleep(0.5)

    resposta = input("Qual foi a sequencia? ")

    vencedor = True
    indice = 0
    for numero in resposta:
        numero = int(numero)
        if lista_frequencias[numero] != lista_sequencia[indice]:
            vencedor = False
        indice += 1

    if vencedor == False:
        print("Você Perdeu")
        break