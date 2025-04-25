import random
def jogo_pedra_papel_tesoura():

    opcoes = ["pedra","papel","tesoura"]

    vitorias_usuario = 0
    vitorias_computador = 0

    while True:
        
        #escolha do computador
        escolha_computador = random.choice(opcoes)

        #escolha do usuario
        escolha_usuario = input("Digite uma das opções: PEDRA, PAPEL OU TESOURA ").lower()

        while escolha_usuario not in opcoes:
            print("OPÇÃO INVÁLIDA")
            escolha_usuario = input("Escolha entre PEDRA, PAPEL OU TESOURA").lower()

        print(f"O computador escolheu: {escolha_computador}")

        if (escolha_usuario == "papel") and (escolha_computador == "pedra") or (escolha_usuario == "tesoura") and (escolha_computador == "papel") or (escolha_usuario == "pedra") and (escolha_computador == "tesoura"):
            print("Você ganhou")
            vitorias_usuario += 1
            
        
        if (escolha_computador == "papel") and (escolha_usuario == "pedra") or (escolha_computador == "tesoura") and (escolha_usuario == "papel") or (escolha_computador == "pedra") and (escolha_usuario == "tesoura"):
            print("Você perdeu")
            vitorias_computador += 1
            
        
        if escolha_usuario == escolha_computador:
            print("Empate Jogue novamente")

        if vitorias_usuario == 3:
            print("Você é o grande vencedor!!!")
            break

        if vitorias_computador == 3:
            print("O computador é o grande vencedor")
            break
        
        print(f"""
            VITORIAS DO USUARIO: {vitorias_usuario}
            VITORIAS DO COMPUTADOR: {vitorias_computador}
            """)
        
        
if __name__ == "__main__":
    jogo_pedra_papel_tesoura()

    