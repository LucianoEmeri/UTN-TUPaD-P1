import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    print(f"\n--- Tabla del {numero} ---")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print("--------------------")

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero"
        
    return (suma, resta, multiplicacion, division)

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# --- Programa Principal ---
if __name__ == "__main__":
    print("--- Ejercicio 1: Hola Mundo ---")
    imprimir_hola_mundo()
    print("-" * 30)

    print("\n--- Ejercicio 2: Saludar Usuario ---")
    nombre_del_usuario = input("Cual es tu nombre? ")
    saludo_personalizado = saludar_usuario(nombre_del_usuario)
    print(saludo_personalizado)
    print("-" * 30)

    print("\n--- Ejercicio 3: Información Personal ---")
    nombre_p = input("Ingresa tu nombre: ")
    apellido_p = input("Ingresa tu apellido: ")
    edad_p = int(input("Ingresa tu edad: "))
    residencia_p = input("Ingresa tu lugar de residencia: ")
    informacion_personal(nombre_p, apellido_p, edad_p, residencia_p)
    print("-" * 30)

    print("\n--- Ejercicio 4: Área y Perímetro del Círculo ---")
    radio_circ = float(input("Ingresa el radio del círculo: "))
    area_calc = calcular_area_circulo(radio_circ)
    perimetro_calc = calcular_perimetro_circulo(radio_circ)
    print(f"El área del círculo es: {area_calc:.2f}")
    print(f"El perímetro del círculo es: {perimetro_calc:.2f}")
    print("-" * 30)

    print("\n--- Ejercicio 5: Segundos a Horas ---")
    segundos_ingresados = int(input("Ingresa una cantidad de segundos: "))
    horas_convertidas = segundos_a_horas(segundos_ingresados)
    print(f"{segundos_ingresados} segundos son {horas_convertidas:.2f} horas.")
    print("-" * 30)

    print("\n--- Ejercicio 6: Tabla de Multiplicar ---")
    num_para_tabla = int(input("De qué número queres ver la tabla de multiplicar? "))
    tabla_multiplicar(num_para_tabla)
    print("-" * 30)

    print("\n--- Ejercicio 7: Operaciones Básicas ---")
    num1_ops = float(input("Ingresa el primer número: "))
    num2_ops = float(input("Ingresa el segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(num1_ops, num2_ops)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")
    print("-" * 30)

    print("\n--- Ejercicio 8: Calcular IMC ---")
    peso_kg = float(input("Ingresa tu peso en kilogramos (ej. 70.5): "))
    altura_mts = float(input("Ingresa tu altura en metros (ej. 1.75): "))
    imc_calculado = calcular_imc(peso_kg, altura_mts)
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc_calculado:.2f}")
    print("-" * 30)

    print("\n--- Ejercicio 9: Celsius a Fahrenheit ---")
    temp_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C son {temp_fahrenheit:.2f}°F.")
    print("-" * 30)

    print("\n--- Ejercicio 10: Calcular Promedio ---")
    num1_prom = float(input("Ingresa el primer número para el promedio: "))
    num2_prom = float(input("Ingresa el segundo número para el promedio: "))
    num3_prom = float(input("Ingresa el tercer número para el promedio: "))
    promedio_final = calcular_promedio(num1_prom, num2_prom, num3_prom)
    print(f"El promedio de los tres números es: {promedio_final:.2f}")
    print("-" * 30)