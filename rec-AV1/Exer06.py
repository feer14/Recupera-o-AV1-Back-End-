6) Dado um array, crie uma função que retorne um novo array sem valores duplicados.

def remover_duplicados(array):
    novo_array = []
    for elemento in array:
        if elemento not in novo_array:
            novo_array.append(elemento)
    return novo_array

# Exemplo de uso:
array = [3, 1, 4, 1, 2, 2, 5, 6, 3, 7]
resultado = remover_duplicados(array)

print(f"Array original: {array}")
print(f"Novo array sem duplicados: {resultado}")
