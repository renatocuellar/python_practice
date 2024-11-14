"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""

palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

palabra1 = palabra1.lower()
palabra2 = palabra2.lower()

palabra1 = palabra1.replace(" ", "")
palabra2 = palabra2.replace(" ", "")

if len(palabra1) != len(palabra2):
    print("No son anagramas")  # Termina aquí si las longitudes no coinciden

palabra1_ordenada = sorted(palabra1)
palabra2_ordenada = sorted(palabra2)

if palabra1_ordenada == palabra2_ordenada:
    print("Son anagramas")
else:
    print("No son anagramas")


# Ahora refactorizado por ChatGPT:

def es_anagrama(palabra1, palabra2):
    # Paso 1: Convertir ambas palabras a minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    # Paso 2: Eliminar espacios
    palabra1 = palabra1.replace(" ", "")
    palabra2 = palabra2.replace(" ", "")
    
    # Paso 3: Verificar si tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False  # Si las longitudes no coinciden, no son anagramas
    
    # Paso 4: Ordenar las letras de ambas palabras
    palabra1_ordenada = sorted(palabra1)
    palabra2_ordenada = sorted(palabra2)
    
    # Paso 5: Comparar las palabras ordenadas
    return palabra1_ordenada == palabra2_ordenada

# Prueba de la función
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

if es_anagrama(palabra1, palabra2):
    print("Son anagramas")
else:
    print("No son anagramas")


"""
Ejercicio: "Palabras Reordenables"
Instrucciones: Escribe una función llamada son_reordenables que tome dos palabras y determine si una es una reordenación parcial de la otra.

Dos palabras son "reordenables parcialmente" si al menos la mitad de las letras en una palabra se pueden encontrar en la otra palabra, aunque no en el mismo orden.

Por ejemplo:

son_reordenables("mar", "armadura") debería devolver True porque al menos la mitad de las letras de "mar" están en "armadura" (m, a y r).
son_reordenables("luz", "sol") debería devolver False porque "sol" no tiene al menos la mitad de las letras de "luz".
Pistas:

Convertir a Minúsculas: Al igual que en el ejercicio anterior, convierte ambas palabras a minúsculas para hacer la comparación insensible a mayúsculas/minúsculas.

Eliminar Espacios: Si decides permitir frases en lugar de palabras individuales, elimina los espacios.

Contar las Letras Comunes: Usa un contador para contar cuántas letras de la primera palabra aparecen en la segunda palabra.

Verificar el Mínimo Requerido: La lógica clave aquí es verificar si el número de letras comunes es al menos la mitad de la longitud de la primera palabra.

Devolver el Resultado: Si hay suficientes letras en común, devuelve True; si no, devuelve False.
"""
def son_reordenables(primera_palabra, segunda_palabra):
    # Paso 1: Convertir ambas palabras a minúsculas
    primera_palabra = primera_palabra.lower()
    segunda_palabra = segunda_palabra.lower()
    
    # Paso 2: Eliminar espacios
    primera_palabra = primera_palabra.replace(" ", "")
    segunda_palabra = segunda_palabra.replace(" ", "")
    
    # Paso 3: Contar letras comunes
    letras_comunes = 0
    for letra in primera_palabra:
        if letra in segunda_palabra:
            letras_comunes += 1
            # Remueve la letra de segunda_palabra para evitar contarla más de una vez
            segunda_palabra = segunda_palabra.replace(letra, "", 1)
    
    # Paso 4: Verificar el mínimo requerido (al menos la mitad de las letras en primera_palabra)
    minimo_requerido = len(primera_palabra) // 2 + len(primera_palabra) % 2
    return letras_comunes >= minimo_requerido

# Prueba de la función
primera_palabra = input("Ingresa la primera palabra: ")
segunda_palabra = input("Ingresa la segunda palabra: ")

if son_reordenables(primera_palabra, segunda_palabra):
    print("True")
else:
    print("False")


