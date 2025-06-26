"""
Entrada
Matriz de enteros de longitud . Los números de la matriz pueden ser cualquier número entero positivo o negativo.0 < arr < 1000

Salida
El índice más bajo, donde el lado a la izquierda de es igual al lado a la derecha de . Si no encuentra un índice que se ajuste a estas reglas, devolverá .NNN-1

Nota
Si se le da una matriz con varias respuestas, devuelva el índice correcto más bajo.
"""
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1