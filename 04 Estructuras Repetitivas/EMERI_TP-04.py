# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for numero in range(101):
    print(numero)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

try:
    numero_str = input("Ingrese un número entero: ")
    numero = int(numero_str)
    numero_positivo = abs(numero)
    cantidad_digitos = len(str(numero_positivo))
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
except ValueError:
    print("Error: La entrada no es un número entero válido.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

try:
    valor1_str = input("Ingrese el primer número entero: ")
    valor1 = int(valor1_str)
    valor2_str = input("Ingrese el segundo número entero: ")
    valor2 = int(valor2_str)

    suma = 0

    if valor1 < valor2:
        for i in range(valor1 + 1, valor2):
            suma += i
    elif valor2 < valor1:
        for i in range(valor2 + 1, valor1):
            suma += i
    else:
        print("Los dos valores ingresados son iguales, no hay números intermedios.")
        suma = None

    if suma is not None:
        print(f"La suma de los números enteros entre {valor1} y {valor2} (excluyendo ambos) es: {suma}")

except ValueError:
    print("Error: Uno o ambos valores ingresados no son números enteros válidos.")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

total = 0
print("Ingrese números enteros para sumar. Ingrese 0 para detener.")

while True:
    try:
        entrada_str = input("Ingrese un número: ")
        numero = int(entrada_str)

        if numero == 0:
            break 
        else:
            total += numero 

    except ValueError:
        print("Error: La entrada no es un número entero válido. Intente de nuevo.")

print(f"El total de los números ingresados es: {total}")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_secreto = random.randint(0, 9)

intentos = 0
adivinado = False

print("¡Bienvenido al juego de adivinar el número!")
print("Intenta adivinar el número secreto entre 0 y 9.")

while not adivinado:
    try:
        intento_str = input("Ingresa tu intento: ")
        intento = int(intento_str)
        intentos += 1

        if intento < numero_secreto:
            print("El número secreto es mayor.")
        elif intento > numero_secreto:
            print("El número secreto es menor.")
        elif intento == numero_secreto:
            adivinado = True
            print(f"¡Felicitaciones! Adivinaste el número secreto ({numero_secreto}) en {intentos} intentos.")

    except ValueError:
        print("Error: La entrada no es un número entero válido. Intenta de nuevo.")
    except KeyboardInterrupt:
        print("\n¡Juego interrumpido!")
        break

if not adivinado and intentos > 0:
    print(f"El número secreto era {numero_secreto}.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for numero in range(100, -1, -2):
    print(numero)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

try:
    limite_str = input("Ingrese un número entero positivo: ")
    limite = int(limite_str)

    if limite < 0:
        print("Error: El número ingresado debe ser positivo.")
    else:
        suma = 0
        for numero in range(limite + 1):
            suma += numero
        print(f"La suma de los números desde 0 hasta {limite} es: {suma}")

except ValueError:
    print("Error: La entrada no es un número entero válido.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad_numeros = 5
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Por favor, ingrese {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    while True:
        try:
            entrada_str = input(f"Ingrese el número {i + 1}: ")
            numero = int(entrada_str)
            break
        except ValueError:
            print("Error: La entrada no es un número entero válido. Intente de nuevo.")

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\n--- Resultados del análisis ---")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 5
suma = 0
numeros_ingresados = []

print(f"Por favor, ingrese {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    while True:
        try:
            entrada_str = input(f"Ingrese el número {i + 1}: ")
            numero = int(entrada_str)
            numeros_ingresados.append(numero)
            suma += numero
            break
        except ValueError:
            print("Error: La entrada no es un número entero válido. Intente de nuevo.")

if cantidad_numeros > 0:
    media = suma / cantidad_numeros
    print("\n--- Resultado del cálculo de la media ---")
    print(f"Los números ingresados fueron: {numeros_ingresados}")
    print(f"La media de los {cantidad_numeros} números es: {media}")
else:
    print("No se ingresaron números para calcular la media.")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

try:
    numero_str = input("Ingrese un número entero: ")
    numero_invertido_str = numero_str[::-1]

    if numero_invertido_str[-1] == '-':
        numero_invertido_str = '-' + numero_invertido_str[:-1]

    print(f"El número invertido es: {numero_invertido_str}")

except ValueError:
    print("Error: La entrada no es un número entero válido.")