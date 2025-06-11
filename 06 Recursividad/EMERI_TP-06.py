import math

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario
def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.
def fibonacci_recursivo(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛^𝑚 = 𝑛 * 𝑛^(𝑚−1). Prueba esta función en un
# algoritmo general.
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        print("Esta función no está diseñada para exponentes negativos directamente con esta fórmula.")
        return None
    else:
        return base * potencia_recursiva(base, exponente - 1)

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
# unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
# procedimiento:
# 1. Dividir el número por 2.
# 2. Guardar el resto (0 o 1).
# 3. Repetir el proceso con el cociente hasta que llegue a 0.
# 4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.
# 🧠Ejemplo:
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".
def decimal_a_binario_recursivo(decimal_num):
    if decimal_num == 0:
        return "0"
    elif decimal_num == 1:
        return "1"
    else:
        resto = decimal_num % 2
        cociente = decimal_num // 2
        return decimal_a_binario_recursivo(cociente) + str(resto)

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la
# pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)
def contar_bloques(n):
    if n <= 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10
        contador = 1 if ultimo_digito == digito else 0
        return contador + contar_digito(numero // 10, digito)


# --- PROGRAMAS PRINCIPALES ---
if __name__ == "__main__":
    # --- Ejercicio 1 ---
    print("--- Ejercicio 1: Factorial Recursivo ---")
    try:
        num_usuario = int(input("Ingresa un número entero positivo para calcular factoriales hasta él: "))
        if num_usuario < 0:
            print("Por favor, ingresa un número positivo.")
        else:
            for i in range(1, num_usuario + 1):
                print(f"El factorial de {i} es: {factorial_recursivo(i)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
    print("-" * 40)

    # --- Ejercicio 2 ---
    print("\n--- Ejercicio 2: Serie de Fibonacci Recursiva ---")
    try:
        limite_fib = int(input("Ingresa hasta qué posición de Fibonacci quieres ver (ej. 10): "))
        if limite_fib < 0:
            print("Por favor, ingresa una posición no negativa.")
        else:
            print(f"Serie de Fibonacci hasta la posición {limite_fib}:")
            for i in range(limite_fib + 1):
                print(f"F({i}) = {fibonacci_recursivo(i)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
    print("-" * 40)

    # --- Ejercicio 3 ---
    print("\n--- Ejercicio 3: Potencia Recursiva ---")
    try:
        base_num = float(input("Ingresa la base (un número): "))
        exp_num = int(input("Ingresa el exponente (un entero positivo): "))
        
        resultado_potencia = potencia_recursiva(base_num, exp_num)
        if resultado_potencia is not None:
            print(f"{base_num} elevado a la {exp_num} es: {resultado_potencia}")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar números correctos.")
    print("-" * 40)

    # --- Ejercicio 4 ---
    print("\n--- Ejercicio 4: Decimal a Binario Recursivo ---")
    try:
        num_decimal = int(input("Ingresa un número entero positivo en base decimal: "))
        if num_decimal < 0:
            print("Por favor, ingresa un número positivo.")
        elif num_decimal == 0: # Caso especial para el 0, ya que el recursivo no lo maneja directamente para el inicio
            print(f"El número {num_decimal} en binario es: 0")
        else:
            print(f"El número {num_decimal} en binario es: {decimal_a_binario_recursivo(num_decimal)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
    print("-" * 40)

    # --- Ejercicio 5 ---
    print("\n--- Ejercicio 5: Es Palíndromo Recursivo ---")
    texto = input("Ingresa una palabra (sin espacios ni tildes): ").lower()
    if es_palindromo(texto):
        print(f"'{texto}' es un palíndromo.")
    else:
        print(f"'{texto}' NO es un palíndromo.")
    print("-" * 40)

    # --- Ejercicio 6 ---
    print("\n--- Ejercicio 6: Suma de Dígitos Recursiva ---")
    try:
        numero_digitos = int(input("Ingresa un número entero positivo: "))
        if numero_digitos < 0:
            print("Por favor, ingresa un número positivo.")
        else:
            print(f"La suma de los dígitos de {numero_digitos} es: {suma_digitos(numero_digitos)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
    print("-" * 40)

    # --- Ejercicio 7 ---
    print("\n--- Ejercicio 7: Contar Bloques de Pirámide Recursivo ---")
    try:
        bloques_base = int(input("Ingresa el número de bloques en el nivel más bajo (n): "))
        if bloques_base < 0:
            print("El número de bloques debe ser positivo.")
        else:
            print(f"Total de bloques necesarios para la pirámide con base {bloques_base}: {contar_bloques(bloques_base)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
    print("-" * 40)

    # --- Ejercicio 8 ---
    print("\n--- Ejercicio 8: Contar Dígito Recursivo ---")
    try:
        num_contar = int(input("Ingresa el número entero positivo: "))
        if num_contar < 0:
            print("El número debe ser positivo.")
        else:
            digito_buscar = int(input("Ingresa el dígito a buscar (0-9): "))
            if not (0 <= digito_buscar <= 9):
                print("El dígito debe estar entre 0 y 9.")
            else:
                if num_contar == 0 and digito_buscar == 0:
                    print(f"El dígito {digito_buscar} aparece 1 vez en {num_contar}.")
                else:
                    print(f"El dígito {digito_buscar} aparece {contar_digito(num_contar, digito_buscar)} veces en {num_contar}.")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar números enteros.")
    print("-" * 40)