def jogo_genius():
    import winsound #Biblioteca de som
    import time #Marcar o tempo
    import random #Escolhe algo aleatoriamente

    lista_frequencias = [300,600,900,1200]
    lista_sequencia = []

    print("Seja bem - vindo ao jogo Genius")
        
    

    input("Pressione ENTER para continuar")

    #Programa que executa a frequência dos sons mostrando os números da lista
    indice = 0
    for frequencia in lista_frequencias:
        print(indice)
        winsound.Beep(frequencia,500)
        time.sleep(1) #Espera x segundos
        indice +=1

    time.sleep(0.5)


    print("Prepare-se para o jogo...")

    while True:
        print("Preste atenção na sequência")

        som_escolhido = random.choice(lista_frequencias)
        lista_sequencia.append(som_escolhido)

        indice = 0
        for frequencia in lista_sequencia:
            winsound.Beep(frequencia, 500)
            time.sleep(0.5)
    
        resposta = input("Qual foi a sequência?: ")

        # Verifica se a resposta é igual ao som aleatório escolhido
        vencedor = True

        if len(lista_sequencia) == len(resposta):
            indice = 0
            for numero in resposta:
                numero = int(numero)
                if lista_frequencias[numero] != lista_sequencia[indice]:
                    vencedor = False
                indice +=1
        else: 
            vencedor == False

if __name__ == "__main__":
    jogo_genius()