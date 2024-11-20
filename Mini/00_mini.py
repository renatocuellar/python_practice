"""###
Ejercicio 1: Verificar un Número Primo
Escribe un programa que pida un número al usuario y verifique si es un número primo.

Instrucciones:
Solicita al usuario que ingrese un número entero positivo.
Comprueba si el número es primo:
Un número es primo si es mayor que 1 y solo divisible por 1 y por sí mismo.
Imprime "Es primo" si cumple la condición o "No es primo" si no.
Pista:
Usa un bucle for para verificar si tiene divisores en el rango de 2 hasta la raíz cuadrada del número.
Usa el operador módulo (%) para verificar si un número es divisible.
###"""

is_prime = int(input("Cuál es el número que quieres verifica"))

def es_primo(is_prime):
    if is_prime < 2:
        return "No es primo"
    for i in range(2, int(is_prime**0.5) + 1):
        if is_prime % i == 0:
            return "No es primo"
    return "Es primo"

print(es_primo)