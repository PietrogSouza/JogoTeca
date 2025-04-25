import random

def palavra_aleatoria():
    #lista das palavras da forca
    
    lista_palavras = ["ABACAXI","MORANGO","MAÇÃ","BANANA","GOIABA",]
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
    pass



if (__name__=="__main__"):
   chute_letra = perguntar_letra()
   print(chute_letra)
    
