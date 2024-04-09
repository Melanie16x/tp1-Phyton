# Se define la funcion que toma dos parametros:
# 'n': el numero total de elementos esperados
# 'lista': la lista que contiene todos los numeros excepto uno
def missing_number(n, lista):
    # Se calcula la suma esperada de todos los numeros utilizando la siguiente formula
    suma_esperada = n * (n + 1) // 2
    # Se suma todos los numeros dados en la lista
    suma_dada = sum(lista)
    # Se calcula el numero faltante restando la suma esperada y la suma dada
    numero_faltante = suma_esperada - suma_dada

    # por ultimo, se retorna el resultado de la resta (el numero faltante)
    return numero_faltante

# caso de prueba
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

print("Todos los casos de prueba han pasado correctamente.")