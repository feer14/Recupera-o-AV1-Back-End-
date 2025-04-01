5)Dado um array de números inteiros, conte quantos são pares e quantos são ímpares.

def contar_pares_impares(array):
    pares = 0
    impares = 0

    for num in array:
        if num % 2 == 0:  # Verifica se o número é par
            pares += 1
        else:  # Se não for par, é ímpar
            impares += 1

    return pares, impares

#Exemplo de uso:
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares, impares = contar_pares_impares(array)

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
