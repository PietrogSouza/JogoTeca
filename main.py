import adivinhacao
import Tabuada
import ImparPar


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
-   # 4 - pedra, papel e tesoura                                         -
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

    elif jogo == 0:
        print("até mais tarde")
        break