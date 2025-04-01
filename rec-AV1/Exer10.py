10) Encontre o subarray contínuo com a maior soma dentro de um array de números inteiros.

def maior_soma_subarray(array):
    max_atual = max_global = array[0]  # Inicializa com o primeiro elemento

    for num in array[1:]:
        max_atual = max(num, max_atual + num)  # Decide se continua somando ou começa novo subarray
        max_global = max(max_global, max_atual)  # Atualiza o maior valor global

    return max_global

#Exemplo de uso:
array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
resultado = maior_soma_subarray(array)

print(f"Array: {array}")
print(f"Maior soma de subarray contínuo: {resultado}")
