import random
print ('Adivinha!')


numero = int(input("Adivinhe um número de 1 a 20: "))

sorteado = random.randint(1,20);

if numero == sorteado:
    print("Número sorteado: ", sorteado)
    print("Você adivinhou!")
    
elif numero != sorteado:
    print("numero sorteado: ", sorteado)
    print("Você errou!")