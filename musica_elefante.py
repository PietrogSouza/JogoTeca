def musica_elefante():

    quantidade_musica = int(input("quantas vezes deseja que a musica seja tocada "))
    contador = 1

    while contador <= quantidade_musica:
        
        if contador == 1:
            print("elefante incomoda muita gente")

        if contador % 2 == 1:
            print(f"{contador} elefantes incomodam muita gente")
        contador += 1

        if contador % 2 == 0:
            print(f"{contador} elefantes incomodam {'incomodam,' * contador} muito mais")

if __name__ == "__main__":
    musica_elefante()