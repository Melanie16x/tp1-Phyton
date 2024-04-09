# Se define la funcion que toma como entrada la cadena de texto
def palindrome_reorder(cadena):
    # Se crea un diccionario para contar la cantidad de apariciones de cada caracter en la cadena
    conteo_caracteres = {}

    # Se cuenta la cantidad de apariciones de cada caracter en la cadena
    for caracter in cadena:
        conteo_caracteres[caracter] = conteo_caracteres.get(caracter, 0) + 1
    
    # Se inicializa contadores y variables para contruir el calindromo
    cantidad_impares = 0
    caracter_impar = ''
    palindromo = []

    # Se recorre el diccionario de conteo de caracteres
    for caracter, conteo in conteo_caracteres.items():
        if conteo % 2 != 0:
            # Si la cantidad de apariciones es impar, se incrementa el contador y guardamos el caracter impar
            cantidad_impares += 1
            caracter_impar = caracter
        # Se extiende la mitad del palindromo con la cantidad de veces que aparece el caracter dividido por 2
        palindromo.extend([caracter] * (conteo // 2))
    
    # Si hay mas de un caracter con cantidad impar, no es posible formar un palindromo
    if cantidad_impares > 1:
        return "NO SOLUTION"
    
    # Se contruye la mitad del palindromo como una cadena
    mitad_palindromo = ''.join(palindromo)

    # Se retorna el palindromo completo, concatenando la mitad del palindromo con el caracter impar
    #  y la reversa de la mitad del palindromo
    return mitad_palindromo + caracter_impar + ''.join(reversed(palindromo))

# Caso de prueba
assert palindrome_reorder("aabbc")=="abcba" or palindrome_reorder("aabbc")=="bacab", "Error en el caso de prueba"

print("Todos los casos de prueba han pasado correctamente.")