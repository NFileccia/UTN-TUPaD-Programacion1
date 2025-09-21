#   1) Crear una lista con las notas de 10 estudiantes. 
#    Mostrar la lista completa. 
#    Calcular y mostrar el promedio. 
#    Indicar la nota más alta y la más baja.

#Crea la lista
notas = [5,7,8,3,10,9,7,4,5,6]

#Imprime listado
print(f"Lista de notas de 10 estudiantes: {notas}")

#Calculo e impresion del promedio de notas
promedio = sum(notas) / len(notas)
print(f"El promedio de notas es: {promedio}")

#Impresion de nota mas alta
nota_alta = notas[4]
print(f"La nota mas alta es: {nota_alta}") 

#Impresion de nota mas aaja
nota_baja = notas[3]
print(f"La nota mas baja es: {nota_baja}")

# 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

#Definir lista vacia para agregar productos
lista_prod = []

# Pedir al usuario que ingrese 5 productos
print("Por favor, ingresa 5 productos:")
for i in range(5):
    producto = input(f"Producto {i + 1}: ")
    titlecase_producto = producto.title()
    lista_prod.append(titlecase_producto) #Agrega productos a la lista creada

# Ordena alfabeticamente lo productos
prod_ordenados = sorted(lista_prod)

print(f"Lista de productos: {prod_ordenados}")

# Pedir al usuario el producto que desea eliminar
prod_eliminar = input("¿Qué producto deseas eliminar de la lista? ")
titlecase_prod_eliminar = prod_eliminar.title()

# Eliminar el producto si se encuentra en la lista
if titlecase_prod_eliminar in prod_ordenados:
    prod_ordenados.remove(titlecase_prod_eliminar)
    print("El producto se ha eliminado correctamente.")
    print("La lista de productos actualizada es:", prod_ordenados)
else:
    print("El producto que intentas eliminar no se encuentra en la lista.")


#3) Generar una lista con 15 números enteros al azar entre 1 y 100. 
#   • Crear una lista con los pares y otra con los impares. 
#   • Mostrar cuántos números tiene cada lista.

import random
numeros_aleatorios = [random.randint(1, 100) for i in range(15)] 

print(f"Lista de numeros aleatorios: {numeros_aleatorios}")

lista_par = []
lista_impar = []

# Iterar sobre la lista aleatoria y encasillar los números
for numero in numeros_aleatorios:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

# Mostrar las listas resultantes y la cantidad de elementos
print("Números pares:", lista_par)
print("Cantidad de números pares:", len(lista_par))
print("Números impares:", lista_impar)
print("Cantidad de números impares:", len(lista_impar))

# 4) Dada una lista con valores repetidos: 
# datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
# • Crear una nueva lista sin elementos repetidos. 
# • Mostrar el resultado. 

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3] # Crear lista
print(datos)

lista_sinrep = [] # Crear lista nueva donde irian sin repetir

# Bucle para iterar los numeros dentro de lista original y anadirlos a una nueva sin repetir
for i in datos:
    if i not in lista_sinrep: #Si el numero no se encuentra en la lista nueva, agregarlo
        lista_sinrep.append(i)

print(f"lista sin repetir: {lista_sinrep}")

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase. 
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
# • Mostrar la lista final actualizada. 

#Crear listado de estudiantes
lista_alumnos = ["Martin","Talia","Nicolas","Ramiro","Belen","Marcelo","Claudia","Matias"]
print(f"Lista de estudiantes: {lista_alumnos}")

#Pregunta de consigna
respuesta = input("Desea agregar un nuevo estudiante o eliminar uno existente? AGREGAR/ELIMINAR ")
uppercase_respuesta = respuesta.upper() #Pasar a mayuscula la respuesta para evitar errores


#Condiciones para agregar el estudiante al listado
if uppercase_respuesta == "AGREGAR":
    nuevo_alumno = input("Ingrese el nombre del nuevo estudiante: ")
    titlecase_nuevo_alumno = nuevo_alumno.title()#Cambiar la primer letra a mayuscula para respetar la sintaxis de la lista
    lista_alumnos.append(titlecase_nuevo_alumno)

#Condiciones para eliminar el estudiante del listado
elif uppercase_respuesta == "ELIMINAR":
    alumno_elim = input("Ingrese el nombre del estudiante existente a eliminar: ")
    titlecase_alumno_elim = alumno_elim.title()
#Cambiar la primer letra a mayuscula para respetar la sintaxis armada y poder encontrarlo en la lista posteriormente    
    if titlecase_alumno_elim in lista_alumnos: #Si el estudiante ingresado se encuentra en la lista, eliminarlo de la misma
        lista_alumnos.remove(titlecase_alumno_elim)
    else:
        print("Por favor, ingrese el nombre del estudiante correcto")

else:
    print("Por favor, elige 'SI' o 'NO'.")

print(f"Lista de estudiantes actualizada: {lista_alumnos}")

#   6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el 
#   último pasa a ser el primero).

#Creo el listado e imprimo
lista = list(range(1,8))
print("Lista de numeros: ",lista)

# Cambio el valor de la lista original
# Realizando la suma del ultimo elemento del listado [lista[-1]]
# Por el listado original sin contar su ultimo elemento lista[:-1].
lista = [lista[-1]] + lista[:-1]

print("Lista de numeros rotada hacia la derecha:", lista)

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una 
# semana. 
# • Calcular el promedio de las mínimas y el de las máximas. 
# • Mostrar en qué día se registró la mayor amplitud térmica.

# La primer columna es para las mínimas y la segunda para las máximas.
temperaturas = []
import random
for i in range(7):
    temp_min = random.randint(0, 15)
    temp_max = random.randint(16, 35)
    temperaturas.append([temp_min, temp_max])

# Crear lista de los dias de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print(f"Temperaturas de la semana: [Minima,Maxima] {temperaturas}")

#Bucle donde se le asigna los dias de la semana con su respectiva temperatura min y max
for i in range(len(dias)):
    dia_actual = dias[i]
    temp_min = temperaturas[i][0]
    temp_max = temperaturas[i][1]
    
    print(f"{dia_actual}: Mínima = {temp_min}°C, Máxima = {temp_max}°C")

# Listas para almacenar las temperaturas mínimas y máximas por separado
minimas = [dias[0] for dias in temperaturas]
maximas = [dias[1] for dias in temperaturas]

# Calcular el promedio usando sum() y len() y mostrarlo
promedio_minimas = sum(minimas) / len(minimas)
promedio_maximas = sum(maximas) / len(maximas)

print(f"Promedio de las temperaturas mínimas: {promedio_minimas}°C")
print(f"Promedio de las temperaturas máximas: {promedio_maximas}°C")

# Calcular la amplitud térmica de cada día y encontrar la máxima
amplitudes = [temp_max - temp_min for temp_min, temp_max in temperaturas]
amplitud_maxima = max(amplitudes) # Se utiliza max() para que devuelva el numero mayor de una lista

# Encontrar el índice del día con la mayor amplitud
dia_amp_max_index = amplitudes.index(amplitud_maxima) # Se utiliza index para identificar la posicion de un elemento

# Mostrar el resultado
dia_mayor_amplitud = dias[dia_amp_max_index]
print(f"El día con la mayor amplitud térmica ({amplitud_maxima}°C) fue el {dia_mayor_amplitud}.")


#   8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#   • Mostrar el promedio de cada estudiante. 
#   • Mostrar el promedio de cada materia. 

# Definimos la matriz de notas

import random
notas = [[random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)],[random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)],[random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)],[random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)],[random.randint(0, 10),random.randint(0, 10),random.randint(0, 10)]]
estudiantes = [["Nicolas"],["Talia"],["Ariel"],["Jaquelin"],["Tomas"]]
materias = [["Matematica"],["Literatura"],["Geografia"]]

# Calcular y mostrar el promedio de cada estudiante
for i in range(len(notas)):
    notas_estudiante = notas[i] # Ingresamos a la lista de notas de cada estudiante
    promedio_estudiante = sum(notas_estudiante) / len(notas_estudiante)
    
# Se utiliza el índice para acceder al nombre del estudiante
    print(f"Promedio del estudiante: {estudiantes[i]}: {promedio_estudiante}")

# Calcular y mostrar el promedio de cada materia
for n in range(len(materias)):
    suma_materia = 0
# Recorremos cada fila para sumar la nota de la materia
    for i in range(len(estudiantes)):
        suma_materia += notas[i][n]
    
    promedio_materia = suma_materia / len(estudiantes)
    print(f"Promedio de la materia: {materias[n]}: {promedio_materia}")


#   9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#   • Inicializarlo con guiones "-" representando casillas vacías. 
#   • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#   • Mostrar el tablero después de cada jugada.

# 1. Inicializar el tablero y las variables del juego
tablero = [["-", "-", "-"],
           ["-", "-", "-"],
           ["-", "-", "-"],]
jugador_actual = "X"
jugadas = 0
ganador = None

# Bucle principal del juego
while jugadas < 9 and ganador is None:
    # Mostrar el tablero
    print("Tablero actual:")
    for fila in tablero:
        salida_fila = ""
        for elemento in fila:
            salida_fila += elemento + " "
        print(salida_fila)

    # Obtener la jugada del jugador actual y validar
    while True:
        print(f"Turno del Jugador '{jugador_actual}'.")
        
        # Validar la fila
        fila_valida = False
        while not fila_valida:
            entrada_fila = input("Ingresa la fila (0, 1, 2): ")
            if len(entrada_fila) == 1:
                # Comprobar si el carácter es un dígito manualmente
                es_digito = False
                if '0' <= entrada_fila <= '9':
                    es_digito = True
                
                if es_digito and 0 <= int(entrada_fila) <= 2:
                    fila = int(entrada_fila)
                    fila_valida = True
                else:
                    print("Entrada no válida. Por favor, ingresa un número entre 0 y 2.")
            else:
                print("Entrada no válida. Por favor, ingresa un solo dígito.")

        # Validar la columna
        columna_valida = False
        while not columna_valida:
            entrada_columna = input("Ingresa la columna (0, 1, 2): ")
            if len(entrada_columna) == 1:
                # Comprobar si el carácter es un dígito manualmente
                es_digito = False
                if '0' <= entrada_columna <= '9':
                    es_digito = True
                
                if es_digito and 0 <= int(entrada_columna) <= 2:
                    columna = int(entrada_columna)
                    columna_valida = True
                else:
                    print("Entrada no válida. Por favor, ingresa un número entre 0 y 2.")
            else:
                print("Entrada no válida. Por favor, ingresa un solo dígito.")

        # Validar si la posición está disponible
        if tablero[fila][columna] == "-":
            tablero[fila][columna] = jugador_actual
            break
        else:
            print("Posición ya ocupada. Intenta de nuevo.")

    # 2. Verificar si hay un ganador después de la jugada
    # Verificar filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != "-":
            ganador = jugador_actual
            break

    # Verificar columnas
    if ganador is None:
        for j in range(3):
            if tablero[0][j] == tablero[1][j] == tablero[2][j] != "-":
                ganador = jugador_actual
                break

    # Verificar diagonales
    if ganador is None:
        if (tablero[0][0] == tablero[1][1] == tablero[2][2] != "-") or \
           (tablero[0][2] == tablero[1][1] == tablero[2][0] != "-"):
            ganador = jugador_actual

    # 3. Cambiar de jugador y avanzar el turno
    if ganador is None:
        if jugador_actual == "X":
            jugador_actual = "O"
        else:
            jugador_actual = "X"
    
    jugadas += 1

# 4. Mostrar el resultado final
print("¡Juego terminado!")
print("Tablero final:")
for fila in tablero:
    salida_fila = ""
    for elemento in fila:
        salida_fila += elemento + " "
    print(salida_fila)

if ganador:
    print(f"¡Felicidades! El Jugador '{ganador}' ha ganado el juego.")
else:
    print("¡Es un empate!")


#   10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#   • Mostrar el total vendido por cada producto. 
#   • Mostrar el día con mayores ventas totales. 
#   • Indicar cuál fue el producto más vendido en la semana. 

# 1. Crear e inicializar la matriz de ventas (4 productos x 7 días)
ventas = [
    [100, 80, 40, 55, 30, 60, 40],   # Producto 1
    [5, 12, 18, 22, 28, 32, 38],    # Producto 2
    [8, 11, 19, 23, 27, 31, 36],    # Producto 3
    [13, 16, 21, 26, 29, 33, 37]     # Producto 4
]

# 2. Calcular el total vendido por cada producto
print("Total de ventas por producto:")
totales_por_producto = []
for fila in ventas:
    total_producto = 0
    for venta in fila:
        total_producto += venta
    totales_por_producto.append(total_producto)
    
for i in range(len(totales_por_producto)):
    print(f"Producto {i + 1}: {totales_por_producto[i]} unidades")

# 3. Calcular el día con mayores ventas totales

totales_por_dia = []
for j in range(len(ventas[0])):  # Recorrer por columnas (días)
    total_dia = 0
    for i in range(len(ventas)):  # Recorrer por filas (productos)
        total_dia += ventas[i][j]
    totales_por_dia.append(total_dia)

dia_max_ventas = 0
ventas_max_dia = 0
for i in range(len(totales_por_dia)):
    if totales_por_dia[i] > ventas_max_dia:
        ventas_max_dia = totales_por_dia[i]
        dia_max_ventas = i + 1

print(f"\nEl día con mayores ventas totales fue el día {dia_max_ventas} con {ventas_max_dia} unidades.")

# 4. Indicar cuál fue el producto más vendido en la semana

producto_mas_vendido = 0
max_ventas_semana = 0

for i in range(len(totales_por_producto)):
    if totales_por_producto[i] > max_ventas_semana:
        max_ventas_semana = totales_por_producto[i]
        producto_mas_vendido = i + 1

print(f"\nEl producto más vendido en la semana fue el Producto {producto_mas_vendido} con un total de {max_ventas_semana} unidades.")
