7) Implemente um algoritmo para ordenar um array de números em ordem crescente.

  def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # Últimos i elementos já estão na ordem correta
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                # Troca os elementos se estiverem na ordem errada
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#Exemplo de uso:
array = [64, 34, 25, 12, 22, 11, 90]
ordenado = bubble_sort(array)

print(f"Array ordenado: {ordenado}")
