import forca_funcoes as funcoes

print("SEJA BEM-VINDO AO JOGO DA FORCA")

palavra_secreta = funcoes.palavra_aleatoria()

funcoes.desenhar_forca(0)

tracos = funcoes.montar_tracos(palavra_secreta)

print(*tracos)

letra = funcoes.perguntar_letra()

tracos = funcoes.verificar_letras(tracos,palavra_secreta,letra)

print(*tracos)


