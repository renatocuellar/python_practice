"""
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

 Bucle while para Contar del 1 al 100:

Usa una variable, por ejemplo, numero, que comience en 1.
Configura el while para que el bucle continúe ejecutándose hasta que numero sea 100 (o menos de 101).
Condiciones para Revisar los Múltiplos:

Para identificar múltiplos de un número en Python, usa el operador módulo %. Este operador calcula el residuo de una división.
Si numero % 3 == 0, significa que numero es múltiplo de 3.
Si numero % 5 == 0, significa que numero es múltiplo de 5.
Si numero % 3 == 0 y numero % 5 == 0, significa que numero es múltiplo de ambos (de 3 y 5 al mismo tiempo).
Orden de las Condiciones:

La condición para los múltiplos de 3 y 5 al mismo tiempo (numero % 3 == 0 y numero % 5 == 0) debería ir antes de las condiciones 
individuales para que puedas capturar el caso de "fizzbuzz" antes de verificar "fizz" y "buzz".
Incrementar el Contador:

No olvides incrementar la variable numero dentro del bucle para que vaya subiendo de 1 en 1 hasta 100.
"""

# Inicializa el contador
numero = 1

# Bucle while para contar hasta 100
while numero <= 100:
    # Condiciones para imprimir "Fizz", "Buzz", o "FizzBuzz"
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
    
    # Incrementa el contador en cada iteración
    numero += 1

"""
Vamos a crear dos ejercicios de practica:
Ejercicio 1: "FooBar" (similar a FizzBuzz)
Instrucciones: Escribe un programa que muestre los números del 1 al 50. Pero realiza las siguientes sustituciones:

Si el número es múltiplo de 4, muestra "Foo".
Si el número es múltiplo de 7, muestra "Bar".
Si el número es múltiplo de 4 y 7 a la vez, muestra "FooBar".
Pistas:

Usa el mismo enfoque que en FizzBuzz, pero con múltiplos de 4 y 7.
Asegúrate de que la condición para "FooBar" (múltiplos de 4 y 7) esté primero.
Puedes utilizar un bucle while o for.
"""

#Iniciar el contador
numer = 1

#Bucle While para contar hasta 50
while numer <= 50:
    #Condiciones para FooBar
    if numer % 4 == 0 and numer % 7 == 0:
        print("FooBar")
    elif numer % 4 == 0:
        print("Foo")
    elif numer % 7 == 0:
        print("Bar")
    else:
        print(numer)

    #Incrementar el contador
    numer += 1

"""
Vamos con el segundo ejercicio, un poco más dificil que el anterior:
Ejercicio 2: "FizzBuzz Prime" (más difícil)
Instrucciones: Escribe un programa que muestre los números del 1 al 100, pero con las siguientes sustituciones:

Si el número es múltiplo de 3, muestra "Fizz".
Si el número es múltiplo de 5, muestra "Buzz".
Si el número es múltiplo de 3 y 5, muestra "FizzBuzz".
Si el número es un número primo, muestra "Prime".
Definición de número primo: Un número primo es un número mayor que 1 que solo tiene dos divisores: 1 y él mismo (por ejemplo, 2, 3, 5, 7, 11, etc.).

Pistas:

Usa la lógica de FizzBuzz como base para los múltiplos de 3 y 5.
Agrega una función auxiliar para verificar si un número es primo. La función debería recibir un número y devolver True si es primo o False si no lo es.
Asegúrate de verificar primero si el número es primo antes de aplicar las condiciones de "Fizz", "Buzz" y "FizzBuzz", 
ya que todos los números primos (excepto el 3 y el 5) no cumplen esas condiciones.
Ejemplo de función para verificar números primos:
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
"""
# Creamos la función para verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Comenzamos con el bucle while para contar hasta 100
es_numero = 1
while es_numero <= 100:
    # Primero verificamos si el número es primo
    if es_primo(es_numero):
        print("Prime")
    elif es_numero % 3 == 0 and es_numero % 5 == 0:
        print("FizzBuzz")
    elif es_numero % 3 == 0:
        print("Fizz")
    elif es_numero % 5 == 0:
        print("Buzz")
    else:
        print(es_numero)
    
    # Incrementamos el contador
    es_numero += 1