"""
1. Calcula la suma de los números del 1 al 100.
"""
# Inicializar la variable para almacenar la suma
suma = 0

# Bucle para recorrer los números del 1 al 100
for numero in range(1, 101):  # range(1, 101) incluye los números del 1 al 100
    suma += numero  # Sumar cada número a la variable suma

# Imprimir el resultado
print("La suma de los números del 1 al 100 es:", suma)

"""
Ejercicio 1: Suma de Números Pares
Enunciado: Encuentra la suma de todos los números pares del 1 al 100.

Pistas:

Usa un bucle para recorrer los números del 1 al 100.
Verifica si un número es par usando el operador módulo (%).
Suma solo los números que sean pares.
"""
#Iniciamos una variable para almacenas nuestra suma
suma_pares = 0

# Bucle para recorrer los números del 1 al 100
for numero in range(1, 101): #Con esto recorremos
    if numero % 2 == 0: #Verificamos si el número es par
        suma_pares += numero # Sumamos solo los pares al numero

print("La suma de los número pares es ", suma_pares) #Damos la respuesta

"""
Ejercicio 2: Producto de Números Impares
Enunciado: Calcula el producto (multiplicación acumulativa) de todos los números 
impares entre 1 y 50.

Pistas:

Inicializa una variable producto con el valor 1 
porque el producto de cualquier número por 1 es el mismo número).
Usa un bucle para recorrer los números del 1 al 50.
Verifica si un número es impar usando el operador módulo (%).
Multiplica solo los números impares a la variable producto.
"""
# Iniciamos nuestra variable para almacenar nuestro producto
producto = 1

#Bucle for para recorrer los número del 1 al 50
for numero in range(1, 51): # Usamos un bucle for para tener el rango de 1 a 50
    if numero % 2 == 1: # Vemos si el numero es impar
        producto *= numero #Multiplicamos cada numero por el anterior

print("La multiplicación de los números del 1 al 50 es: ", producto) #Damos la respuesta

"""
Ejercicio 3: Suma de los Cuadrados
Enunciado: Encuentra la suma de los cuadrados de los números del 1 al 50.

Pistas:

Usa un bucle para recorrer los números del 1 al 50.
Calcula el cuadrado de cada número usando número ** 2.
Suma el cuadrado de cada número a una variable acumuladora llamada suma_cuadrados.
"""
# Iniciamos nuestra variable para almacenar nuestro producto
suma_cuadrados = 0

#Bucle for para recorrer los número del 1 al 50
for numero in range(1, 51): # Usamos un bucle for para tener el rango de 1 a 50
    suma_cuadrados += (numero ** 2) #Sumamos solo los cuadrados de una a 50

print("La suma de todos los cuadrados de 1 a 50 es: ", suma_cuadrados) #Damos la repsuesta