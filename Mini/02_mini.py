"""
Ejercicio 3: FizzBuzz Mejorado
Escribe un programa que imprima los números del 1 al 50. Sin embargo:

Si un número es múltiplo de 3, imprime "Fizz".
Si un número es múltiplo de 5, imprime "Buzz".
Si un número es múltiplo de ambos, imprime "FizzBuzz".
Instrucciones:
Usa un bucle for para recorrer del 1 al 50.
Verifica las condiciones para múltiplos de 3 y 5.
Imprime el resultado según las reglas.
Pista:
Usa condicionales if con los operadores módulo (%).
"""

numero = 1
bucle = [0, 51]

for numero in bucle:
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
    numero += 1


# Corrección

# Bucle FizzBuzz
for numero in range(1, 51):  # Recorrer números del 1 al 50
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
