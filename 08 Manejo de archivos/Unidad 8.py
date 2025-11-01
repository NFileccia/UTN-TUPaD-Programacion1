# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado 
# productos.txt con tres productos. Cada línea debe tener:  nombre,precio,cantidad 

# Abrir (o crear) el archivo en modo escritura "w"
with open("productos.txt", "w", encoding="utf-8") as archivo: # encoding="utf-8" asegura compatibilidad con tildes o caracteres especiales.
    # Escribir tres productos (nombre, precio, cantidad)
    archivo.write("Remera,400,20\n")
    archivo.write("Jeans,350,15\n")
    archivo.write("Zapatos,200,35\n")

print("Archivo 'productos.txt' creado correctamente.")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada 
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente 
# formato: 
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

# Abrir el archivo en modo lectura "r"
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo: # ciclo for para leer las lineas del archivo
        linea = linea.strip() # Quitar espacios y salto de línea al final
        nombre, precio, cantidad = linea.split(",") # Separar los valores por coma (nombre, precio, cantidad)
        
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar 
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, 
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

print("Stock de productos:\n") 

# Mostrar stock
with open("productos.txt", "r", encoding="utf-8") as archivo: 
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# Solicitar nuevo producto al usuario
print("\nIngresar nuevo producto:")

nombre = input("Nombre del producto: ").capitalize()
# Validar que el precio y cantidad sean numéricos
while True:
    precio = input("Precio del producto: ").replace(",", ".")
    if precio.replace('.', '', 1).isdigit(): # Validacion de numero entero y/o decimal
        break
    else:
        print("Ingrese un valor numérico válido para el precio.")

while True:
    cantidad = input("Cantidad en stock: ")
    if cantidad.isdigit():
        break
    else:
        print("Ingrese un número entero válido para la cantidad.")

# Agregar el nuevo producto al final del archivo (sin borrar lo anterior)
with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nombre},{precio},{cantidad}\n")

print(f"\nProducto '{nombre}' agregado correctamente al archivo.")
# Mostrar stock actualizado.
with open("productos.txt", "r", encoding="utf-8") as archivo: 
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en 
# una lista llamada productos, donde cada elemento sea un diccionario con claves: 
# nombre, precio, cantidad.

productos = []  # lista vacía donde se guardarán los diccionarios

# Leer el archivo línea por línea
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()  # elimina espacios y saltos de línea
        if linea:  # evita procesar líneas vacías
            nombre, precio, cantidad = linea.split(",")
            producto = { # Crea diccionario por cada producto
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto) # carga los diccionarios a la lista

# Mostrar los productos cargados
print("Lista de productos cargada desde el archivo:\n")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un 
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si 
# no existe, mostrar un mensaje de error. 

# Cargar productos desde el archivo en una lista de diccionarios
productos = []
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea = linea.strip()
        if linea:
            nombre, precio, cantidad = linea.split(",")
            productos.append({
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            })

print(" Productos disponibles:") # Mostrar los productos cargados (solo nombres)
for p in productos:
    print(f"- {p['nombre']}")

busqueda = input("\n Ingrese el nombre del producto que desea buscar: ").capitalize()

encontrado = False # boole para verificar si se encontró

for p in productos: # Buscar en la lista
    if p["nombre"].capitalize() == busqueda:
        print(f"\nProducto encontrado:")
        print(f"Nombre: {p['nombre']}")
        print(f"Precio: ${p['precio']}")
        print(f"Cantidad: {p['cantidad']}")
        encontrado = True
        break  # termina la búsqueda

if not encontrado:
    print(f"\n El producto '{busqueda}' no existe en el archivo.")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado 
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los 
# productos actualizados desde la lista.

productos = [ # Cargar desde listado donde cada elemento es un diccionario
    {"nombre": "Remera", "precio": 400, "cantidad": 20},
    {"nombre": "Jeans", "precio": 350, "cantidad": 15},
    {"nombre": "Zapatos", "precio": 200, "cantidad": 35},
    {"nombre": "Buzos", "precio": 200, "cantidad": 10},
    {"nombre": "Campera", "precio": 150, "cantidad": 40}
]

# Sobrescribir el archivo con los datos actualizados
with open("productos.txt", "w", encoding="utf-8") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print("\nArchivo 'productos.txt' actualizado correctamente.\n")