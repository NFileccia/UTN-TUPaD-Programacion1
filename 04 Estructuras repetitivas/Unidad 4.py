#   1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#   (incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 

num = 0

for num in range(0,101,1):
    print(num)

#   2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#   dígitos que contiene. 

#Definicion de variables
num = int(input("Ingresa un numero entero: "))
cant_digitos = 0

#En caso de que se ingrese 0
if num == 0:
    cant_digitos = 1
else:
    while num > 0: #Bucle utilizando la cantidad de divisiones entera del numero ingresado aumenta la cantidad de digitos
        num = num // 10
        cant_digitos += 1
print(f"El numero ingresado tiene {cant_digitos} digitos")

#   3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#   dados por el usuario, excluyendo esos dos valores. 

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese otro numero: "))

suma = 0

for i in range(num1+1,num2): #Se define i como iterador quien realiza la suma a la variable propiamente dicha y se agrega +1 a num1 excluyendo el mismo
    suma += i

print(f"La suma de todos los valores comprendidos entre los numeros dados es:{suma}")

#   4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#   secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#   un 0. 

num = int(input("Ingrese un numero entero: "))
suma = 0

while num != 0:
    suma += num 
    num = int(input("Ingrese un numero entero: "))
    
print(f"El total acumulado de la suma de numeros ingresados es: {suma}")

#   5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#   programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

print("Vamos a Jugar! Adivina el numero aleatorio: (0/9)")

num_aleatorio = 5
intentos = 0

while intentos >= 0:
    num = int(input("Ingrese un numero: "))
    intentos += 1

    if num < num_aleatorio:
        print("Demasiado bajo, vuelva a intertarlo.")
    elif num > num_aleatorio:
        print("Demasiado alto, vuelva a intertarlo.")
    else:
        num == num_aleatorio
        print(f"FELICIDADES, adivinaste el numero en {intentos} intentos.")
        break

#   6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#   entre 0 y 100, en orden decreciente. 

num = 100

for num in range(100,-2,-2):
    print(num)

#   7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#   número entero positivo indicado por el usuario. 

num1 = 0
num2 = int(input("ingrese un numero: "))

suma = 0

for i in range(num1,num2+1): #Se define i como iterador quien realiza la suma a la variable propiamente dicha y se agrega +1 a num2 incluyendo el mismo
    suma += i

print(f"La suma de todos los valores comprendidos entre los numeros dados es:{suma}")

#   8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#   programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#   negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#   menor, pero debe estar preparado para procesar 100 números con un solo cambio).


#Definicion de variables
cantidad = 100
par = 0
impar = 0
neg = 0
pos = 0

for i in range(cantidad): #Bucle de 100 numeros
	num = int(input(f"Ingrese un numero {i+1}: "))
	
	if num % 2 == 0: #Par o Impar
		par += 1
	else: impar += 1
	
	if num > 0: #Positivo o Negativo
		pos += 1
	elif num < 0:
		neg += 1
	else: pass
    
#Resultado
print(f"Numeros pares: {par} Numeros positivos: {pos} Numeros negativos: {neg} Numeros impares: {impar}")

#   9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#   media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#   poder procesar 100 números cambiando solo un valor). 


#Definicion de variables
cantidad = 100
suma = 0

print(f"Ingrese {cantidad} numeros enteros: ")

for i in range(cantidad):
    numeros = int(input(f"Ingrese un numero {i+1}: "))
    suma += numeros

media = suma / cantidad

print(f"La media de los {cantidad} numeros es: {media}.")

#   10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#   usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 

numero = int(input("Ingrese un número: "))
num_invertido = 0

while numero > 0:
    digito = numero % 10
    num_invertido = num_invertido * 10 + digito
    numero //= 10
    
print(f"El número invertido es: {num_invertido}")
