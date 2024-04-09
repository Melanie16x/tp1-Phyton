# Se crea una lista vacia para almacenar los numeros generados por el algoritmo
lista = []

# Se define una funcion que toma como entrada un numero
def weird_algorithm (numero):
    # Se agrega el numero inicial como primer elemento de la lista
    lista.append(numero)

    # Se utiliza el bucle 'while' para indicar que 'mientras el numero sea diferente a 1' se ingresa al bucle
    while numero != 1:
        # se usa una condicion 'si el numero es par'
        if numero % 2 == 0:
            # Si se cumple la condicion se divide el numero por 2 y se agrega a la lista
            numero = numero // 2
            lista.append(numero)
        else:
            # si el numero es impar, se multiplica el por 3 y se suma 1, luego se agrega a la lista
            numero = numero * 3 + 1
            lista.append(numero)

    # una vez que se llega a 1, se retorna la lista de numeros generados
    return lista

# caso de prueba
assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

print("Todos los casos de prueba han pasado correctamente.")