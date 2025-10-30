# TP 6 Funciones.

#  1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#  2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de
# volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):    
    print(f"Hola {nombre}!")

nombre = input("Ingrese su nombre: ")

saludar_usuario(nombre)

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
# los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
while True:
    edad = input("Ingrese su edad: ")
# Solo realice la validacion en edad porque no hay prohibicion en los demas parametros que tengan digitos en el
    if not edad.isdigit():  
        print("Ingrese un numero porfavor para su edad.")
    else:
        break
residencia = input("Ingrese el lugar donde vive: ")
    

informacion_personal(nombre,apellido,edad,residencia)

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra
# dio como parámetro y devuelva el área del círculo. calcular_peri
# metro_circulo(radio) que reciba el radio como parámetro y devuel
# va el perímetro del círculo. Solicitar el radio al usuario y llamar am
# bas funciones para mostrar los resultados.

import math # Se importa modulo math de python para realizar el calculo que incluye pi

def calcular_area_circulo(radio): # Función para calcular el área de un círculo
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio): # Función para calcular el perímetro (circunferencia)
    return 2 * math.pi * radio
    
print("Calcular el area y perimetro de un circulo!")

# Solicitar el radio al usuario con validación
while True:
    numero = input("\nIngrese el radio del círculo: ").replace(",", ".") # Permite usar coma o punto como separador decimal.
    if numero.count(".") <= 1 and numero.replace(".", "").isdigit(): # Validar que sea número decimal o entero positivo
        radio = float(numero) # .replace permite usar coma o punto como separador decimal
        if radio > 0:          # .count permite contar los puntos "." asignando como 1 de validacion
            break
        else:
            print("El radio debe ser mayor que cero.")
    else:
        print("Error: debe ingresar un número decimal válido. Intente de nuevo.")

# Calcular resultados
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Mostrar resultados
print(f"\nÁrea del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}") # .2f muestra el resultado con solo dos decimales

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.


# Función para convertir segundos a horas, minutos y segundos
def segundos_a_horas(segundos):
    horas = int(segundos // 3600)                 # División entera para obtener horas completas
    minutos = int((segundos % 3600) // 60)        # Resto de horas, convertido a minutos
    segundos_restantes = int(segundos % 60)       # Resto final de segundos
    return horas, minutos, segundos_restantes

print("\nConvertimos segundos a horas!")

# Solicitar al usuario los segundos (con validación)
while True:
    numero = input("Ingrese la cantidad de segundos: ").replace(",", ".")
    if numero.count(".") <= 1 and numero.replace(".", "").isdigit():
        segundos = float(numero) # .replace permite usar coma o punto como separador decimal
        if segundos > 0: # .count permite contar los puntos "." asignando como 1 de validacion
            break
        else:
            print("El valor debe ser mayor que cero.")
    else:
        print("Error: debe ingresar un número decimal válido. Intente de nuevo.")

# Calcular la conversión
horas, minutos, segundos_restantes = segundos_a_horas(segundos)

# Mostrar resultado
print(f"\n{segundos:.0f} segundos equivalen a:") # .0f devuelve float sin decimales
print(f"{horas} horas, {minutos} minutos y {segundos_restantes} segundos.")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):  # Función
    print(f"\nabla de multiplicar del {numero}:")
    for num in range(1, 11): # numero del 1 al 10
        print(f"{numero} x {num} = {numero * num}")

print("\nTabla de multiplicar del 1 al 10!")

while True: # Validación
    entrada = input("Ingrese un número para ver su tabla de multiplicar: ")
    if entrada.isdigit():  # valida que sean solo números enteros positivos
        numero = int(entrada)
        if numero > 0:
            break
        else:
            print("Debe ingresar un número mayor que cero.")
    else:
        print("Ingrese solo números enteros, sin letras ni símbolos.")

tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos 
# números como parámetros y devuelva una tupla con el resultado de sumarlos,
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Evitamos división por cero
    division = a / b if b != 0 else "No se puede dividir por 0"
    return (suma, resta, multiplicacion, division)

while True:
    a = input("Ingrese el primer número: ")
    if a.replace('.', '', 1).isdigit(): # Validacion de digitos con coma/punto
        a = float(a)
        break
    else:
        print("Error: ingrese un número válido (entero o decimal).")

# Solicitar el segundo número
while True:
    b = input("Ingrese el segundo número: ")
    if b.replace('.', '', 1).isdigit(): # Validacion de digitos con coma/punto
        b = float(b)
        break
    else:
        print("Error: ingrese un número válido (entero o decimal).")

resultados = operaciones_basicas(a, b)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

while True: # Validar peso con digitos decimales
    peso = input("Ingrese su peso en kilogramos: ").replace(",", ".")
    if peso.replace('.', '', 1).isdigit():
        peso = float(peso)
        if peso > 0:
            break
        else:
            print("El peso debe ser mayor que cero.")
    else:
        print("Ingrese un número válido para el peso (use punto o coma si es decimal).")

while True: # Validar altura con digitos decimales
    altura = input("Ingrese su altura en metros: ").replace(",", ".")
    if altura.replace('.', '', 1).isdigit():
        altura = float(altura)
        if altura > 0:
            break
        else:
            print("La altura debe ser mayor que cero.")
    else:
        print("Ingrese un número válido para la altura (use punto o coma si es decimal).")

imc = calcular_imc(peso, altura)

print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

while True: # Validacion 
    numero = input("Ingrese la temperatura en grados Celsius: ").replace(",", ".")
    if numero.replace('.', '', 1).isdigit(): # Validar número entero o decimal
        celsius = float(numero)
        break
    else:
        print("Error: ingrese un valor numérico válido (use punto o coma si es decimal).")

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

# Definición de la función
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

while True: # Validacion de numeros ingresados
    a = input("Ingrese el primer número: ").replace(",", ".")
    b = input("Ingrese el segundo número: ").replace(",", ".")
    c = input("Ingrese el tercer número: ").replace(",", ".")

    if (a.replace('.', '', 1).isdigit() and # Se utilizan las mismas validaciones de numeros enteros y decimales
        b.replace('.', '', 1).isdigit() and
        c.replace('.', '', 1).isdigit()):
        a = float(a) # Convertir a flotantes
        b = float(b)
        c = float(c)
        break
    else:
        print("Error: asegúrese de ingresar solo números válidos (enteros o decimales).\n")

promedio = calcular_promedio(a, b, c)

print(f"El promedio de {a}, {b} y {c} es: {promedio:.2f}")