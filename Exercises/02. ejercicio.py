"""
Ejercicio Completo: Gestor de Inventario
Contexto:
Eres responsable de desarrollar un sistema básico de inventario para una tienda en línea. 
El inventario debe:

Permitir agregar nuevos productos.
Mostrar la lista de productos con sus detalles (nombre, precio, cantidad disponible).
Buscar un producto por nombre y actualizar su cantidad o precio.
"""

"""
Parte 1: Crear la estructura del inventario
Objetivo:
Diseñar una estructura para almacenar los productos. Cada producto debe tener:

nombre: Nombre del producto.
precio: Precio del producto.
cantidad: Cantidad disponible en el inventario.
Instrucciones:
Usa un diccionario para representar el inventario.
Cada clave será el nombre del producto.
El valor será otro diccionario con las claves precio y cantidad.
Crea una función agregar_producto que permita añadir un nuevo producto al inventario. 
La función debe:
Recibir como parámetros el nombre, precio y cantidad del producto.
Añadir el producto al diccionario del inventario.
Si el producto ya existe, debe mostrar un mensaje indicando que el producto ya está registrado.
Pista:
Inicializa el inventario como un diccionario vacío: inventario = {}.
Usa if nombre in inventario para verificar si el producto ya existe.
"""

# Inventario inicial vacío
inventario = {}

# Función para agregar un producto
def agregar_producto(inventario, nombre, precio, cantidad):
    # Verificar si el producto ya existe
    if nombre in inventario:
        print("El producto ya está registrado.")
    else:
        # Agregar el producto al inventario
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}
        print(f"Producto {nombre} agregado correctamente.")

# Probar la función
agregar_producto(inventario, "Laptop", 1000, 5)
agregar_producto(inventario, "Mouse", 20, 50)
agregar_producto(inventario, "Laptop", 1200, 3)  # Este debería mostrar un mensaje de "ya registrado"
agregar_producto(inventario, "LaptopGamer", 1500, 50)
agregar_producto(inventario, "MousePad", 5, 10)

# Ver el inventario actual
print(inventario)

"""
Parte 2: Mostrar el inventario
Objetivo:
Crear una función mostrar_inventario que imprima la lista completa de productos 
con sus precios y cantidades.

Instrucciones:
La función debe recorrer el diccionario inventario y mostrar cada producto.
Formatea la salida para que sea fácil de leer. Ejemplo:
makefile
Copiar código
Producto: Laptop
Precio: $1000
Cantidad: 5
---------------
Pista:
Usa un bucle for para iterar sobre el diccionario.
Accede a los valores del producto con inventario[clave]["precio"].
"""
def mostrar_inventario(inventario):
    if not inventario:  # Verifica si el inventario está vacío
        print("El inventario está vacío.")
        return
    
    for nombre in inventario:
        print(f"Producto: {nombre}")
        print(f"Precio: ${inventario[nombre]['precio']}")
        print(f"Cantidad: {inventario[nombre]['cantidad']}")
        print("-" * 20)  # Línea divisoria

mostrar_inventario(inventario)

"""
Parte 3: Actualizar el inventario
Objetivo:
Crear una función actualizar_producto que permita:

Buscar un producto por su nombre.
Actualizar su precio o cantidad según lo que el usuario desee.
Si el producto no existe, muestra un mensaje indicando que no se encontró.
Instrucciones:
Solicita al usuario el nombre del producto.
Si el producto existe:
Pregunta si desea actualizar el precio o la cantidad.
Actualiza el valor correspondiente.
Si no existe, muestra un mensaje indicando que no se encontró.
Pista:
Usa input para preguntar qué valor se desea actualizar.
Modifica el valor en el diccionario usando su clave: inventario[nombre]["precio"].
"""

def actualizar_producto(inventario):
    # Solicitar el nombre del producto a actualizar
    nombre_producto = input("Ingresa el nombre del producto a actualizar: ")

    # Verificar si el producto existe en el inventario
    if nombre_producto in inventario:
        print(f"Producto encontrado: {nombre_producto}")
        # Preguntar al usuario qué desea actualizar
        opcion = input("¿Qué deseas actualizar? (precio/cantidad): ").lower()
        
        if opcion == "precio":
            # Actualizar el precio
            nuevo_precio = float(input("Ingresa el nuevo precio: "))
            inventario[nombre_producto]["precio"] = nuevo_precio
            print(f"El precio de '{nombre_producto}' ha sido actualizado a ${nuevo_precio:.2f}")
        
        elif opcion == "cantidad":
            # Actualizar la cantidad
            nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
            inventario[nombre_producto]["cantidad"] = nueva_cantidad
            print(f"La cantidad de '{nombre_producto}' ha sido actualizada a {nueva_cantidad} unidades.")
        
        else:
            print("Opción no válida. Por favor, elige entre 'precio' o 'cantidad'.")
    else:
        # Producto no encontrado
        print(f"El producto '{nombre_producto}' no se encuentra en el inventario.")
