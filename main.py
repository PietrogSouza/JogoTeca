import adivinhacao

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

#Perguntando qual jogo será jogado
jogo = int(input("informe o jogo escolhido: "))
#Verificando qual jogo foi escolhido
if jogo == 1:
    adivinhacao.jogo_adivinhacao()