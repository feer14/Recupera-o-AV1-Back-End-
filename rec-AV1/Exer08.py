8) Desloque todos os elementos de um array para a direita (ou esquerda).
 
 def deslocar_direita(array, n):
    n = n % len(array)  # Garante que o deslocamento não ultrapasse o tamanho do array
    return array[-n:] + array[:-n]

#Exemplo de uso:
array = [1, 2, 3, 4, 5]
deslocado = deslocar_direita(array, 2)

print(f"Array original: {array}")
print(f"Array deslocado para a direita: {deslocado}")
