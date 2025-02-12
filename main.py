print("Contagem de Vogais")

string = "Uma frase qualquer"
cont = 0  # Contador

vogais = "aeiouAEIOU"  # Conjunto de vogais

# Percorre cada caractere da string
for letra in string:
    if letra in vogais:  # Verifica se a letra está no conjunto de vogais
        cont += 1  # Incrementa o contador

print("A quantidade de vogais é:", cont)
