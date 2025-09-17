#   1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
#   deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.


edad = int(input(f"Ingrese su edad: "))

if  edad > 18:
    print("Eres mayor de edad")
else: print("No eres mayor de edad")

#   2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#   mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el 
#   mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))

if nota >= 6:  
    print("Aprobado")
else:
    print("Desaprobado")

#   3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#   número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#   contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#   operador de módulo (%) en Python para evaluar si un número es par o impar. 

num = int(input("Ingrese un numero: "))

if num % 2 == 0:
    print("Ha ingresado un numero par")

else: print("Por favor, ingrese un numero par")

#   4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#   siguientes categorías pertenece: 
#   ● Niño/a: menor de 12 años. 
#   ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#   ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#   ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad < 12:
    print("Eres un Niño/a")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un Adulto/a joven")
elif edad >= 30:
    print("Eres un Adulto/a")
else:
    pass

#   5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#   (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#   pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#   pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#   de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#   como una lista o un string.

password = input("Ingrese una contraseña (Debe tener entre 8 y 14 caracteres): ")

longitud_pass = len(password)

if longitud_pass >= 8 and longitud_pass <= 14:
    print("Ha ingresado una contraseña correcta")
else: print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#   6) Escribir un programa que tome la lista 
#   numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#   hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean 
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

print(f"mode:",mode(numeros_aleatorios))
print(f"median:",median(numeros_aleatorios))
print(f"mean:",mean(numeros_aleatorios))

if (mean(numeros_aleatorios) > median(numeros_aleatorios)) and (median(numeros_aleatorios) > mode(numeros_aleatorios)):
    print("Hay sesgo positivo o a la derecha")
elif (mean(numeros_aleatorios) < median(numeros_aleatorios)) and (median(numeros_aleatorios) < mode(numeros_aleatorios)):
    print("Hay sesgo negativo o a la izquierda")
elif (mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios)):
    print("No hay sesgo")

#   7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#   termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#   pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
#   pantalla.

frase = input("Ingrese una palabra o frase:")
vocal1 = "a"
vocal2 = "e"
vocal3 = "i"
vocal4 = "o"
vocal5 = "u"

ultimo_caracter = frase[-1]

if ultimo_caracter == vocal1:
    print(frase,"!")
elif ultimo_caracter == vocal2:
    print(frase,"!")
elif ultimo_caracter == vocal3:
    print(frase,"!")
elif ultimo_caracter == vocal4:
    print(frase,"!")
elif ultimo_caracter == vocal5:
    print(frase,"!")
else: print(frase)

#   8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#   dependiendo de la opción que desee: 
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#   El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#   usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#   lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")
opcion = int(input("Ingrese una opcion (1, 2, 3): "))

if opcion == 1:
    uppercase_nombre = nombre.upper()
    print(uppercase_nombre)
elif opcion == 2:
    lowercase_nombre = nombre.lower()
    print(lowercase_nombre)
elif opcion == 3:
    titlecase_nombre = nombre.title()
    print(titlecase_nombre)
else: pass

#   9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#   magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#   por pantalla: 
#   ● Menor que 3: "Muy leve" (imperceptible). 
#   ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#   ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#   generalmente no causa daños). 
#   ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#   débiles). 
#   ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#   ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

terremoto = float(input("Ingrese la magnitud de un terremoto en escala Richter: "))

if terremoto > 0 and terremoto < 3:
    print("Muy leve (imperceptible).")
elif terremoto >= 3 and terremoto < 4 :
    print("Leve (ligeramente perceptible).")
elif terremoto >= 4 and terremoto < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif terremoto >= 5 and terremoto < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif terremoto >= 6 and terremoto < 7:
    print("Muy Fuerte (puede causar daños significativos).")
elif terremoto >= 7:
    print("Extremo (puede causar graves daños a gran escala).")
else: pass

#   10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#   del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#   si el usuario se encuentra en otoño, invierno, primavera o verano. 

emisferio = input("En cuál hemisferio se encuentra (N/S): ")
uppercase_emisferio = emisferio.upper() # Pasar a MAYUSCULA la tecla n/s de corresponder.

mes = (input("Que mes del año es? "))
titlecase_mes = mes.title() # Pasar primer letra a MAYUSCULA en caso de corresponder.

dia = int(input("Que dia es? "))

# Asignacion de variables correspondientes al cuadro de estaciones emisferio N/S.

invierno_n = uppercase_emisferio == "N" and (titlecase_mes == "Diciembre" and (dia >= 21 and dia <= 31)) or (titlecase_mes == "Enero" and (dia >= 1 and dia <= 31)) or (titlecase_mes == "Febrero" and (dia >= 1 and dia <= 29)) or (titlecase_mes == "Marzo" and (dia >= 1 and dia <= 20))

primavera_n = uppercase_emisferio == "N" and (titlecase_mes == "Marzo" and (dia >= 21 and dia <= 31)) or (titlecase_mes == "Abril" and (dia >= 1 and dia <= 30)) or (titlecase_mes == "Mayo" and (dia >= 1 and dia <= 31)) or (titlecase_mes == "Junio" and (dia >= 1 and dia <= 20))

verano_n = uppercase_emisferio == "N" and (titlecase_mes == "Junio" and (dia >= 21 and dia <= 30)) or (titlecase_mes == "Julio" and (dia >= 1 and dia <= 31)) or (titlecase_mes == "Agosto" and (dia >= 1 and dia <= 31)) or (titlecase_mes == "Septiembre" and (dia >= 1 and dia <= 20))

otonio_n = uppercase_emisferio == "N" and (titlecase_mes == "Septiembre" and (dia >= 21 and dia <= 30)) or (titlecase_mes == "Octubre" and (dia >= 1 and dia <= 31)) or (titlecase_mes == "Noviembre" and (dia >= 1 and dia <= 30)) or (titlecase_mes == "Diciembre" and (dia >= 1 and dia <= 20))

verano_s = uppercase_emisferio == "S" and (titlecase_mes == "Diciembre" and (dia >= 21 and dia <= 31)) or (titlecase_mes == "Enero" and (dia >= 1 and dia <= 31)) or (titlecase_mes == "Febrero" and (dia >= 1 and dia <= 29)) or (titlecase_mes == "Marzo" and (dia >= 1 and dia <= 20))

otonio_s = uppercase_emisferio == "S" and (titlecase_mes == "Marzo" and (dia >= 21 and dia <= 31)) or (titlecase_mes == "Abril" and (dia >= 1 and dia <= 30)) or (titlecase_mes == "Mayo" and (dia >= 1 and dia <= 31)) or (titlecase_mes == "Junio" and (dia >= 1 and dia <= 20))

invierno_s = uppercase_emisferio == "S" and (titlecase_mes == "Junio" and (dia >= 21 and dia <= 30)) or (titlecase_mes == "Julio" and (dia >= 1 and dia <= 31)) or (titlecase_mes == "Agosto" and (dia >= 1 and dia <= 31)) or (titlecase_mes == "Septiembre" and (dia >= 1 and dia <= 20))

primavera_s = uppercase_emisferio == "S" and (titlecase_mes == "Septiembre" and (dia >= 21 and dia <= 30)) or (titlecase_mes == "Octubre" and (dia >= 1 and dia <= 31)) or (titlecase_mes == "Noviembre" and (dia >= 1 and dia <= 30)) or (titlecase_mes == "Diciembre" and (dia >= 1 and dia <= 20))

# Condiciones dependiendo de los datos que ingresen.

if invierno_n:
    print("Usted se encuentra en Invierno")
elif primavera_n:
    print("Usted se encuentra en Primavera")
elif verano_n:
    print("Usted se encuentra en Verano")
elif otonio_n:
    print("Usted se encuentra en Otoño")
elif verano_s:
    print("Usted se encuentra en Verano")
elif otonio_s:
    print("Usted se encuentra en Otoño")
elif invierno_s:
    print("Usted se encuentra en Invierno")
elif primavera_s:
    print("Usted se encuentra en Primavera")
else: pass