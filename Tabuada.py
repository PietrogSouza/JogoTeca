import random
numero_aleatorio1 = random.randint(1,10)
numero_aleatorio2 = random.randint(1,10)
resultado = numero_aleatorio1*numero_aleatorio2
print(f" {numero_aleatorio1}x{numero_aleatorio2}")
chute=int(input("me diga o resultado"))
if chute ==resultado:
    print(f"Parabens você acertou")
else:
    print(f"você errou o resultado é: {resultado}")




