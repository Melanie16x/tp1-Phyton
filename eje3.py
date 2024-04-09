# Define una matriz que representa a las primeras 5 capas del espiral numerico
espiral = [
    [1, 2, 9, 10, 25],
    [4, 3, 8, 11, 24],
    [5, 6, 7, 12, 23],
    [16, 15, 14, 13, 22],
    [17, 18, 19, 20, 21]
]
# Se define una funcion llamada 'number_spiral' que toma tres argumentos: columna, fila y espiral
# La funcion devuelve el valor de la celda en la posicion (fila, columna) de la matriz 'espiral'
def number_spiral(columna, fila, espiral):
    return espiral[fila-1][columna-1] if 0 <= fila-1 < len(espiral) and 0 <= columna-1 < len(espiral[0]) else None

# Casos de prueba
assert number_spiral(2, 2, espiral) == 3, "Error en el caso de prueba"

print("Todos los casos de prueba han pasado correctamente.")