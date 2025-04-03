import random

def jogo_adivinhacao():
    #Menu de dificuldade 
    print("""
    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
    ¨¨    1 - NÍVEL FÁCIL (1 á 10)       ¨¨
    ¨¨    2 - NÍVEL MÉDIO (1 á 20)       ¨¨
    ¨¨    3 - NÍVEL DIFICIL (1 á 50)     ¨¨
    ¨¨    4 - NÍVEL SENAI (1 á 100)      ¨¨
    ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨
    """)
    menu_nivel = int(input("Escolha um dos níveis acima: "))
    valor_maximo = 0

    if menu_nivel == 1: 
        print ("Você escolheu o nivel 1 fácil")
        valor_maximo = 10

    elif menu_nivel == 2: 
        print("Você escolheu o nivel 2 médio")
        valor_maximo = 20

    elif menu_nivel == 3:
        print ("Você escolheu o nivel 3 dificil")
        valor_maximo = 50


    elif menu_nivel == 4:
        print("Você escolheu o nivel 4 SENAI")
        valor_maximo = 100

    else:
        print("Este nivel não existe, escolha um dos niveis sugerido acima")

    #Escolhe um número aleatório
    if valor_maximo > 1 :
        numero_aleatorio = random.randint (1,valor_maximo)

        while True:
            # Perguntar o número
            numero_usuario = int(input(f"Digite um número entre 1 à {valor_maximo}: "))

        #Verificando se ele ganhou
            if numero_usuario == numero_aleatorio:
                print("Você acertou!!")
                break
            else: 
                print (f"Você errou o número era {numero_aleatorio}")


if __name__ == "__main__":
 jogo_adivinhacao()