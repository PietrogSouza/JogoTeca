import forca_funcoes as funcoes

def jogo_forca():

    print("SEJA BEM-VINDO AO JOGO DA FORCA")

    palavra_secreta = funcoes.palavra_aleatoria()

    tracos = funcoes.montar_tracos(palavra_secreta)

    erro = 0

    while True:
        funcoes.desenhar_forca(erro)
        
        print(*tracos)

        letra = funcoes.perguntar_letra()

        if letra in palavra_secreta:
            tracos = funcoes.verificar_letras(tracos,palavra_secreta,letra)
        else:
            erro += 1
            print("Você errou, tente outra letra")
        
        print(*tracos)

        if "_" not in tracos:
            funcoes.fim_de_jogo("VITÓRIA")
            break
        
        if erro == 7:
            funcoes.desenhar_forca(erro)
            funcoes.fim_de_jogo("DERROTA")
            print(f"a palavra era {palavra_secreta}")
            break

if __name__ == "__main__":
    jogo_forca()
