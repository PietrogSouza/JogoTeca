import random
opcoes = ["pedra","papel","tesoura"]
while True:
    
    #escolha do computador
    escolha_computador = random.choice(opcoes)

    #escolha do usuario
    escolha_usuario = input("Digite uma das opções: PEDRA, PAPEL OU TESOURA ").lower()

    while escolha_usuario not in opcoes:
        print("OPÇÃO INÁLIDA")
        escolha_usuario = input("Escolha entre PEDRA, PAPEL OU TESOURA").lower()
        
    if (escolha_usuario == "papel") and (escolha_computador == "pedra") or (escolha_usuario == "tesoura") and (escolha_computador == "papel") or (escolha_usuario == "pedra") and (escolha_computador == "tesoura"):
        print("Você ganhou")
        break
    if (escolha_computador == "papel") and (escolha_usuario == "pedra") or (escolha_computador == "tesoura") and (escolha_usuario == "papel") or (escolha_computador == "pedra") and (escolha_usuario == "tesoura"):
        print("Você perdeu")
        break
    if (escolha_usuario == "papel") and (escolha_computador == "papel") or (escolha_usuario == "tesoura") and (escolha_computador == "tesoura") or (escolha_usuario == "pedra") and (escolha_computador == "pedra"):
        print("Empate Jogue novamente")

    print(f"você escolheu {escolha_usuario} e o computador escolheu {escolha_computador}")