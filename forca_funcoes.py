import random

def palavra_aleatoria():
    #lista das palavras da forca

    #usamos o open para abrir o arquivo .txt para o ler com o .read
    # usamos split para quebrar o enter dentro do arquivo  
    #logo apos usamos close para fecha-lo
    arquivo = open("fpalavras.txt","r")
    lista_palavras = arquivo.read().split()
    print(arquivo.read())
    arquivo.close()
    
    # with open("palavras.txt", "r") ass arquivo:
    #       lista_palavras = arquivo.read().split()
    
    palavra_escolhida = random.choice(lista_palavras)
    return palavra_escolhida
    
def desenhar_forca(erros):
    #desenhando a forca pela quantidade de erros
    
    if erros == 0:
        print(""" 
              
            ________________
            |/             ! 
            |           
            |
            |
            |
            |  
            |                            
            |  
           _|___________________   """)
    
    
    elif erros == 1:
        print("""
            _______________
            |/            ! 
            |           (._.)
            |
            |
            |
            |  
            |                            
            |  
           _|___________________   """)
        
    elif erros == 2:
        print("""
            _______________
            |/            ! 
            |           (._.)
            |             |
            |             |
            |
            |  
            |                            
            |  
           _|___________________   """)    
    

    elif erros == 3:
        print("""
            _______________
            |/            ! 
            |           (._.)
            |            /|
            |             |
            |
            |  
            |                            
            |  
           _|___________________   """)    
        

    elif erros == 4:
        print("""
            _______________
            |/            ! 
            |           (._.)
            |            /|\\
            |             |
            |            
            |  
            |                            
            |  
           _|___________________   """)   
        

    elif erros == 5:
        print("""
            _______________
            |/            ! 
            |           (._.)
            |            /|\\
            |             |
            |            /
            |  
            |                            
            |  
           _|___________________   """)   
        


    elif erros == 6:
        print("""
            _______________
            |/            ! 
            |           (._.)
            |            /|\\
            |             |
            |            / \\
            |  
            |                            
            |  
           _|___________________   """)   
        

    
    elif erros == 7:
        print("""
            _______________
            |/            ! 
            |           (x_x)
            |            /|\\
            |             |
            |            / \\
            |  
            |                            
            |  
           _|___________________   """)   

def perguntar_letra():

    #perguntar letra
    #tranformar a letra em maiuscula
    #se a quantidade de letras na reposta for diferente de 1, diga que é invalido e volte a perguntar 
    #retorne a letra       
     
    chute_letra = input("chute uma letra: ")
    quant_letra = len(chute_letra)
    while quant_letra != 1:
        print("ERRO LETRA INVÁLIDA, TENTE NOVAMENTE")
        chute_letra = input("chute outra letra: ")
        quant_letra = len(chute_letra)
    return chute_letra.upper()

def fim_de_jogo(resultado):
    if resultado == "VITÓRIA":
        fim_de_jogo == "VITÓRIA"
        print("Parabens você ganhou!!!")

    if resultado == "DERROTA":
        fim_de_jogo == "DERROTA"
        print("Hahaha você perdeu")

def montar_tracos(palavra) -> list[str]:
    tracos = []
    contador = 0
    qtdeletras = len(palavra)
    while contador < qtdeletras:
        tracos.append("_")
        contador = contador + 1
    return tracos

def verificar_letras(tracos,palavra,letra) -> list[str]:
    contador = 0
    for letra_percorrida in palavra:
        if letra_percorrida == letra:
            tracos[contador] = letra
        contador += 1
    return tracos

        




if (__name__=="__main__"):
    tracos = montar_tracos("AMORA")
    tracos = verificar_letras(tracos,"AMORA","A")
    print(*tracos)
