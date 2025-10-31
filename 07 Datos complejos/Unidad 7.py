# 1) Dado el diccionario precios_frutas 
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
# Añadir las siguientes frutas con sus respectivos precios: 
#● Naranja = 1200 
#● Manzana = 1500 
#● Pera = 2300 

# Definimos el diccionario
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}
print("Diccionario de frutas:")
print(precios_frutas)
# Agregar nuevas frutas con sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar el diccionario actualizado
print("Diccionario de frutas actualizado:")
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: 
# ● Banana = 1330 
# ● Manzana = 1700 
# ● Melón = 2800 

# Diccionario actualizado del punto anterior
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}
print("Diccionario con precios:")
print(precios_frutas)

# Actualizar los precios indicados
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el diccionario final con los nuevos valores
print("Diccionario con precios actualizados:")
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
# precios. 

# Diccionario del punto anterior
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Lista con las frutas
lista_frutas = list(precios_frutas.keys())

# Mostrar la lista
print("Lista de frutas:")
print(lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. 
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

# --- Programa: Agenda telefónica ---

# Crear diccionario vacío
agenda = {}

# Cargar 5 contactos
print("Carga de contactos telefónicos")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de teléfono de {nombre}: ")
    agenda[nombre] = numero  # guarda nombre como clave y número como valor
    print("Contacto agregado correctamente.\n")

print(agenda)

# Consultar un contacto
print("Consulta de número telefónico")
consulta = input("Ingrese el nombre del contacto a buscar: ")

# Buscar en el diccionario
if consulta in agenda:
    print(f"El número de {consulta} es: {agenda[consulta]}")
else:
    print(f"No existe un contacto registrado con el nombre '{consulta}'.")

# 5) Solicita al usuario una frase e imprime: 
# • Las palabras únicas (usando un set). 
# • Un diccionario con la cantidad de veces que aparece cada palabra.

# Solicitar una frase al usuario
frase = input("Ingrese una frase: ").lower()

palabras = frase.split() # Separar la frase en palabras

palabras_unicas = set(palabras)

frecuencias = {} # Crear un diccionario con la cantidad de repeticiones

for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1  # .get() para el programa no se detenga con error si la keys no existe

# Mostrar resultados
print("\nPalabras únicas:")
print(palabras_unicas)

print("\nCantidad de veces que aparece cada palabra:")
print(frecuencias)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. 
# Luego, mostrá el promedio de cada alumno. 

alumnos = {}  # diccionario vacío para guardar los datos

# 2 bucle for para crear los nombres con las notas
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")

    notas = []  # lista temporal para guardar las 3 notas
    for j in range(3):
        while True:
            n = input(f"Ingrese la nota {j+1} de {nombre}: ").replace(",", ".") # notas validadas
            if n.replace('.', '', 1).isdigit():
                nota = float(n)
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
            else:
                print("Error: ingrese solo números (use punto o coma si es decimal).")

        alumnos[nombre] = tuple(notas) # pasaje de lista a tupla y guardar en el diccionario
        print(f"Nota {j+1} de {nombre} cargado correctamente.\n")

print(f"\n{alumnos}") # mostrar diccionario
print("\nPromedio de cada alumno:") # mostrar promedio de nota de cada alumno
for nombre in alumnos:
    notas = alumnos[nombre]
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
# y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales. 
# • Mostrá los que aprobaron solo uno de los dos. 
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir). 

# Conjuntos de estudiantes aprobados por parcial
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {104, 105, 106, 107, 108}

print("\nListado de alumnos por Nro de legajo que aprobaron los parciales 1 y 2:")
print(f"\nAprobados en parcial 1: {parcial1}")
print(f"Aprobados en parcial 2: {parcial2}")

ambos = parcial1 & parcial2 # Interseccion

solo_uno = parcial1 ^ parcial2 # Diferencia simetrica

al_menos_uno = parcial1 | parcial2 # Union

print(f"Aprobados en ambos parciales: {ambos}")
print(f"Aprobados solo en uno de los dos: {solo_uno}")
print(f"Aprobados en al menos uno: {al_menos_uno}")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
# Permití al usuario: 
# • Consultar el stock de un producto ingresado. 
# • Agregar unidades al stock si el producto ya existe. 
# • Agregar un nuevo producto si no existe.

# Diccionario inicial con productos y su stock
stock_productos = {
    "Remeras": 17,
    "Jeans": 24,
    "Camperas": 15,
    "Zapatillas": 20
}

print("Sistema de control de stock\n")
print("Productos actuales y su stock:")
for producto in stock_productos: # Muestra el stock actual
    cantidad = stock_productos[producto]
    print(f" - {producto}: {cantidad} unidades")

producto = input("\nIngrese el nombre del producto que desea consultar: ").capitalize() # Pone en mayuscula la primer letra de la cadena de str

if producto in stock_productos:
    print(f"El producto '{producto}' existe. Stock actual: {stock_productos[producto]} unidades.") # Verifica si el producto existe
    while True:
        agregar = input(f"¿Desea agregar unidades al stock de {producto}? (si/no): ").lower() # Agrega cantidad de stock del producto existente validado
        if agregar == "si":
            cantidad = input("Ingrese la cantidad a agregar: ")
            if cantidad.isdigit():
                cantidad = int(cantidad)
                stock_productos[producto] += cantidad
                print(f"Stock actualizado. Ahora hay {stock_productos[producto]} unidades de {producto}.")
                break
            else:
                print("Por favor ingrese un número entero válido.")
        elif agregar == "no":
            print("No se realizaron cambios en el stock.")
            break
        else:
            print("Opción no válida. Responda con 'si' o 'no'.")
else:     # Si el producto no existe, preguntar si desea agregarlo validado
    print(f"El producto '{producto}' no existe en el sistema.")
    while True:
        nuevo = input("¿Desea agregarlo al stock? (si/no): ").lower()
        if nuevo == "si":
            while True:
                cantidad = input("Ingrese la cantidad inicial de stock: ")
                if cantidad.isdigit():
                    stock_productos[producto] = int(cantidad)
                    print(f"Producto '{producto}' agregado con {cantidad} unidades en stock.")
                    break
                else:
                    print("Por favor ingrese un número entero válido.")
        elif nuevo == "no":
            print("No se agregó ningún producto nuevo.")
            break
        else:
            print("Opción no válida. Responda con 'si' o 'no'.")

# Mostrar el stock actualizado
print("\nStock final actualizado:")
for producto in stock_productos:
    cantidad = stock_productos[producto]
    print(f" - {producto}: {cantidad} unidades")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. 
# Ejemplo: Permití consultar qué actividad hay en cierto día y hora.

# Diccionario de agenda
agenda = {
    ("Lunes", "14:00"): "Clases de Ingles",
    ("Martes", "19:00"): "Futbol",
    ("Miercoles", "09:30"): "Reunion de trabajo",
    ("Jueves", "21:00"): "Cena familiar",
    ("Viernes", "16:00"): "Entrega de proyecto",
    ("Sabado", "20:00"): "Casamiento",
    ("Domingo", "17:00"): "Futbol"
}

print("Agenda semanal")
for clave in agenda:
    dia, hora = clave  # desempaquetamos la tupla
    print(f" - {dia} a las {hora}: {agenda[clave]}")

print("\nConsulta de actividad")

dias_validos = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
while True:
    dia = input("Ingrese el día que desea consultar: ").capitalize()
    if dia in dias_validos:
        break
    else:
        print("Día inválido. Ingrese un día de la semana válido (por ejemplo: Lunes, Martes, etc.).")

while True:
    hora = input("Ingrese la hora (formato HH:MM): ").strip() # Validar la hora (formato HH:MM)

    # Validar estructura básica del horario
    if ":" in hora:
        partes = hora.split(":")
        if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
            horas, minutos = int(partes[0]), int(partes[1])
            # Validar rango horario
            if 0 <= horas <= 23 and 0 <= minutos <= 59:
                break
            else:
                print("La hora debe estar entre 00:00 y 23:59.")
        else:
            print("Ingrese la hora con formato correcto, por ejemplo 09:30 o 14:00.")
    else:
        print("El formato debe incluir dos puntos (:), por ejemplo 08:15.")

# Buscar el evento
clave_busqueda = (dia, hora)

if clave_busqueda in agenda:
    print(f"El evento del {dia} a las {hora} es: {agenda[clave_busqueda]}")
else:
    print(f"No hay actividades registradas el {dia} a las {hora}.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
# diccionario donde: 
# • Las capitales sean las claves. 
# • Los países sean los valores. 

# Diccionario original
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia",
    "Paraguay": "Asunción"
}

capitales = {} # Nuevo diccionario vacio

for pais, capital in paises.items(): # .items recorre el diccionario por pares (clave:valor)
    capitales[capital] = pais # Se invierte los valores con las claves y se guarda en el nuevo diccionario

# Mostrar resultados
print("Diccionario original (País: Capital):")
print(paises)

print("\nDiccionario invertido (Capital: País):")
print(capitales)