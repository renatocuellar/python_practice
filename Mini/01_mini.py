"""
Ejercicio 2: Palíndromo de Palabras
Escribe un programa que determine si una palabra ingresada por el usuario es un palíndromo.

Instrucciones:
Solicita al usuario una palabra.
Ignora las mayúsculas o minúsculas (usa .lower() para convertir todo a minúsculas).
Compara la palabra con su reverso.
Imprime "Es un palíndromo" si coincide o "No es un palíndromo" si no.
Pista:
Usa slicing ([::-1]) para obtener la palabra invertida.
"""

es_palindromo = input("Cuál es tu palabra")

def palindromo(es_palindromo):
    #Convertir la palabra en minuscula
    es_palindromo = es_palindromo.lower()
    #comparar la palabra
    if es_palindromo == es_palindromo.slicing[::-1]:
        return "Es un palíndromo"
    else:
        return "No es un palíndromo"
    
print(palindromo(es_palindromo))


# Corrección

# Solicitar palabra al usuario
es_palindromo = input("¿Cuál es tu palabra? ")

# Función para verificar si es palíndromo
def palindromo(palabra):
    # Convertir la palabra a minúsculas
    palabra = palabra.lower()
    # Comparar la palabra con su reverso
    if palabra == palabra[::-1]:
        return "Es un palíndromo"
    else:
        return "No es un palíndromo"

# Imprimir el resultado
print(palindromo(es_palindromo))
