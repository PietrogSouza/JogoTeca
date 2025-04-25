import adivinhacao
import Tabuada
import ImparPar
import Jokenpo
import musica_elefante
import genius
while True:
    print("""
                                            (`-')      (`-')  _           (`-')  _  
                .->       .->        .->   ( OO).->   ( OO).-/ _         (OO ).-/  
    <-.--.(`-')----.  ,---(`-')(`-')----. /    '._  (,------. \-,-----. / ,---.   
    (`-'| ,|( OO).-.  ''  .-(OO )( OO).-.  '|'--...__) |  .---'  |  .--./ | \ /`.\  
    (OO |(_|( _) | |  ||  | .-, \( _) | |  |`--.  .--'(|  '--.  /_) (`-') '-'|_.' | 
    ,--. |  | \|  |)|  ||  | '.(_/ \|  |)|  |   |  |    |  .--'  ||  |OO )(|  .-.  | 
    |  '-'  /  '  '-'  '|  '-'  |   '  '-'  '   |  |    |  `---.(_'  '--'\ |  | |  | 
    `-----'    `-----'  `-----'     `-----'    `--'    `------'   `-----' `--' `--' 
    """)
    while True:
        print("""
    ----------------------------------------------
    -                                            -                                            
    -   # 1 - Jogo de Adivinhação                -
    -   # 2 - Jogo da Tabuada                    -
    -   # 3 - Jogo Par ou Impar                  -
    -   # 4 - pedra, papel e tesoura             -
    -   # 5 - musica do elefante                 -
    -   # 6 - Genius                             -    
    -   # 0 - Sair                               -                              
    -                                            -
    -                                            -
    ----------------------------------------------
    """)

        #Perguntando qual jogo será jogado
        jogo = int(input("Olá, qual jogo você gostaria de jogar? "))
        #Verificando qual jogo foi escolhido
        
        if jogo == 1:
            adivinhacao.jogo_adivinhacao()

        elif jogo == 2:
            Tabuada.jogo_tabuada()

        elif jogo == 3:    
            ImparPar.jogo_Impar_Par()

        elif jogo == 4:
            Jokenpo.jogo_pedra_papel_tesoura()
        
        elif jogo == 5:
            musica_elefante.musica_elefante()

        elif jogo == 6:
            genius.jogo_genius()    

        elif jogo == 0:
            print("foi um prazer jogar com você, até mais tarde")
            break