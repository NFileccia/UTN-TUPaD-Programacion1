# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
# función para calcular y mostrar en pantalla el factorial de todos los números enteros 
# entre 1 y el número que indique el usuario 

# Función recursiva que calcula el factorial
def factorial(n):
    if n == 0 or n == 1: # Caso base
        return 1
    else: # Caso recursivo
        return n * factorial(n - 1)

while True: # Solicita el numero para el calculo con validacion
    entrada = input("Ingrese un numero entero positivo: ")
    if entrada.isdigit():
        numero = int(entrada)
        break
    else:
        print("Ingrese solo números enteros positivos.")

print(f"\nFactoriales del 1 al {numero}:")
for i in range(1, numero + 1):
    print(f"{i}! = {factorial(i)}") # resultado

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
# especifique. 

def fibonacci(n): # Función recursiva de Fibonacci
    if n == 0:  # Caso base
        return 0       
    elif n == 1:
        return 1             
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Caso recursivo

while True: # Solicitar al usuario la cantidad de términos
    entrada = input("Ingrese la cantidad de términos de la serie Fibonacci: ")
    if entrada.isdigit():
        cantidad = int(entrada)
        if cantidad > 0:
            break
    print("Ingrese un número entero positivo mayor que 0.")

# Mostrar la serie completa
print(f"\nSerie de Fibonacci con {cantidad} términos:")
for i in range(cantidad):
    print(f"Posición {i}: {fibonacci(i)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un 
# exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un 
# algoritmo general. 

# Función recursiva para calcular la potencia n^m
def potencia(base, exponente):
    if exponente == 0: # Caso base
        return 1
    else: # Caso recursivo
        return base * potencia(base, exponente - 1)

# Algoritmo general
while True: # Solicitud de ingresos de valores base y exponentes validadas
    num_base = input("Ingrese la base: ").replace(",", ".")
    num_exp = input("Ingrese el exponente (entero no negativo): ")

    if num_base.replace('.', '', 1).lstrip('-').isdigit() and num_exp.isdigit():
        base = float(num_base)
        exponente = int(num_exp)
        break
    else:
        print("Ingrese valores válidos. La base debe ser numérica y el exponente un entero no negativo.")

# Calcular y mostrar el resultado
resultado = potencia(base, exponente)
print(f"\nResultado: {base}^{exponente} = {resultado}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base 
# decimal y devuelva su representación en binario como una cadena de texto. 

# Función recursiva
def decimal_a_binario(n):
    if n == 0:
        return "0"  # Caso base
    elif n == 1:
        return "1"
    else: # Caso recursivo donde la división entera y residuo, construye la cadena de atrás hacia adelante
        return decimal_a_binario(n // 2) + str(n % 2)

# --- Algoritmo general ---
while True:
    num = input("Ingrese un número entero positivo: ")
    if num.isdigit() and int(num) >= 0:
        numero = int(num)
        break
    else:
        print("Ingrese solo números enteros positivos.")

# Mostrar el resultado
print(f"\nEl número {numero} en binario es: {decimal_a_binario(numero)}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una 
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no 
# lo es. 
# Requisitos: 
# La solución debe ser recursiva. 
# No se debe usar [::-1] ni la función reversed(). 

def es_palindromo(palabra):
    if len(palabra) <= 1: # Caso base, si la palabra tiene <= 1 letra
        return True
    elif palabra[0] == palabra[-1]: # Caso recursivo, comparar primera y ultima letra
        return es_palindromo(palabra[1:-1]) # Slicing para recortar la palabra sin la primera y ultima letra
    else: # Si las letras no coinciden, no es palíndromo
        return False

palabra = input("Ingrese una palabra (sin espacios ni tildes): ").lower().strip() # Entrada validada

if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un 
# número entero positivo y devuelva la suma de todos sus dígitos. 
# Restricciones: 
# No se puede convertir el número a string. 
# Usá operaciones matemáticas (%, //) y recursión. 
# Ejemplos: 
# suma_digitos(1234)   → 10  (1 + 2 + 3 + 4) 
# suma_digitos(9)      → 9 
# suma_digitos(305)    → 8   (3 + 0 + 5)

def suma_digitos(n):
    if n < 10: # Caso base: si el número tiene un solo dígito, devolverlo directamente
        return n
    else: # Caso recursivo: sumar el último dígito + la suma del resto
        return (n % 10) + suma_digitos(n // 10)
    # n % 10: devuelve el ultimo digito
    # n // 10: elimina el ultimo digito
    # recursion: ultimo digito + n(sin ultimo digito)

while True: # Solicitud validada
    entrada = input("Ingrese un número entero positivo: ")
    if entrada.isdigit():
        numero = int(entrada)
        break
    else:
        print("Ingrese solo números enteros positivos.")

print(f"\nLa suma de los dígitos de {numero} es: {suma_digitos(numero)}")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n 
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al 
# último nivel con un solo bloque. 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el 
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la 
# pirámide. 
# Ejemplos: 
# contar_bloques(1)   → 1         (1) 
# contar_bloques(2)   → 3         (2 + 1) 
# contar_bloques(4)   → 10        (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1: # Caso base se necesita solo 1 bloque
        return 1
    else: # Caso recursivo: bloque actual + bloques del resto de la pirámide
        return n + contar_bloques(n - 1)

while True: # Solicitud validada
    num = input("Ingrese la cantidad de bloques en el nivel más bajo: ")
    if num.isdigit() and int(num) > 0:
        niveles = int(num)
        break
    else:
        print("Ingrese un número entero positivo mayor que 0.")

print(f"\nPara construir una pirámide con {niveles} bloques en la base, se necesitan {contar_bloques(niveles)} bloques en total.")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un 
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces 
# aparece ese dígito dentro del número. 
# Ejemplos: 
# contar_digito(12233421, 2)   → 3   
# contar_digito(5555, 5)       → 4   
# contar_digito(123456, 7)     → 0

def contar_digito(numero, digito):
    if numero == 0: # Caso base
        return 0
    else: # extraer el ultimo digito
        ultimo = numero % 10
        if ultimo == digito:
            return 1 + contar_digito(numero // 10, digito) # suma 1 si hay coincidencia
        else:
            return contar_digito(numero // 10, digito)

while True:
    n_num = input("Ingrese un número entero positivo: ")
    n_dig = input("Ingrese el dígito a buscar (0-9): ")
    # solicitud validada
    if n_num.isdigit() and n_dig.isdigit() and 0 <= int(n_dig) <= 9:
        numero = int(n_num)
        digito = int(n_dig)
        break
    else:
        print("Ingrese valores válidos (número entero positivo y dígito entre 0 y 9).")

print(f"\nEl dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}.")

