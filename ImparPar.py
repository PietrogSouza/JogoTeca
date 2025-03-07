import random
imparpar = input("impar ou par: ")

numero1 = random.randint(1,10)
numero2 = int(input("me diga um numero "))

print(f"o meu numero é: {numero1}")

resultado1 = numero1 + numero2
resultado2 = resultado1 % 2

if (imparpar == "impar" and resultado2 == 1) or (imparpar == "par" and resultado2 == 0):
    print("Parabens, você ganhou")
else:
    print("Você Perdeu")