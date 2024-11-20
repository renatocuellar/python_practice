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