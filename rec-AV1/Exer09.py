9) Dado dois arrays, retorne um novo array contendo apenas os elementos presentes em ambos (interseção).

def intersecao_arrays(array1, array2):
    return [elemento for elemento in array1 if elemento in array2]

#Exemplo de uso:
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
resultado = intersecao_arrays(array1, array2)

print(f"Array 1: {array1}")
print(f"Array 2: {array2}")
print(f"Interseção: {resultado}")
