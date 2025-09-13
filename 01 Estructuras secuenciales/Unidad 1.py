# TP 1 Secuenciales - FILECCIA Nicolas Ariel

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input("Escriba su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.

nombre = input("Escriba su nombre: ")

apellido = input("Escriba su apellido: ")

edad = int(input("Escriba su edad: "))

lugar = input("Escriba su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

radio = int(input("Escriba el radio de un cirulo:"))

area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio

print(f"Si radio es: {radio}, el area del circulo es: {area} y el perimetro del circulo es: {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = int(input("Escriba una cantidad de segundos:"))

minutos = (segundos % 3600) // 60

hora =  segundos // 3600

segundos_restantes = segundos % 60

print(segundos,"segundos, equivalen a",hora,"horas",minutos,"minutos y",segundos_restantes,"segundos")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
# multiplicar de dicho número.  

numero = int(input("Ingrese un numero: "))

print(f"Tabla de multiplicacion (1 al 10) del numero: ",numero,)

print(f"1*",numero,"=",numero*1)
print(f"2*",numero,"=",numero*2)
print(f"3*",numero,"=",numero*3)
print(f"4*",numero,"=",numero*4)
print(f"5*",numero,"=",numero*5)
print(f"6*",numero,"=",numero*6)
print(f"7*",numero,"=",numero*7)
print(f"8*",numero,"=",numero*8)
print(f"9*",numero,"=",numero*9)
print(f"10*",numero,"=",numero*10)

#   7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
#   pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

num_1 = int(input("Ingrese un numero:"))
num_2 = int(input("Ingrese un numero:"))

suma = num_1+num_2
div = num_1/num_2
mult = num_1*num_2
resta = num_1-num_2

print(f"Suma:{num_1}+{num_2}=",suma)
print(f"Division:{num_1}/{num_2}=",div)
print(f"Multiplicacion:{num_1}*{num_2}=",mult)
print(f"Resta:{num_1}-{num_2}=",resta)

#   8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#   de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente 
#   modo:  

altura = float(input("Ingrese su altura (m):"))
peso = float(input("Ingrese su peso (kg):"))

imc = peso / (altura**2)

print(f"El IMC segun su altura y peso es de:{imc}")

#   9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
#   pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 

temp_c = int(input("Ingrese una temperatura en grados Celsius: "))

temp_f = (9/5 * temp_c) + 32

print(f"{temp_c} grados Celsius son equivalentes a {temp_f} grados Fahrenheit")

#   10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
#   dichos números. 

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))

prom = (num1+num2+num3)/3

print(f"El promedio de los numeros: {num1}, {num2}, {num3} es {prom}")