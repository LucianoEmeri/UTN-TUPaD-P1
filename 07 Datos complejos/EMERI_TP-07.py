# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
def ejecutar_ejercicio_1(precios_iniciales):
    print(" Ejercicio 1 ")
    precios = precios_iniciales.copy() 
    precios['Naranja'] = 1200
    precios['Manzana'] = 1500
    precios['Pera'] = 2300
    print("Diccionario después de añadir Naranja, Manzana y Pera:", precios)
    return precios

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800
def ejecutar_ejercicio_2(precios_actuales):
    print(" Ejercicio 2 ")
    precios = precios_actuales.copy()
    precios['Banana'] = 1330
    precios['Manzana'] = 1700
    precios['Melón'] = 2800
    print("Diccionario después de actualizar los precios de Banana, Manzana y Melón:", precios)
    return precios

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.
def ejecutar_ejercicio_3(precios_actuales):
    print(" Ejercicio 3 ")
    lista_frutas = list(precios_actuales.keys())
    print("Lista de frutas sin precios:", lista_frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
def programa_telefonos():
    contactos = {}
    print(" Ejercicio 4 ")
    print("Por favor, carga 5 contactos:")
    for i in range(5):
        nombre = input(f"Ingresa el nombre del contacto {i+1}: ")
        numero = input(f"Ingresa el número de teléfono de {nombre}: ")
        contactos[nombre] = numero

    print("\nContactos cargados:", contactos)

    nombre_buscar = input("\nIngresa el nombre del contacto que quieres buscar: ")

    if nombre_buscar in contactos:
        print(f"El número de teléfono de {nombre_buscar} es: {contactos[nombre_buscar]}")
    else:
        print(f"El contacto '{nombre_buscar}' no se encuentra en la agenda.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
def analizar_frase():
    print(" Ejercicio 5 ")
    frase_usuario = input("Ingresa una frase: ")
    palabras = frase_usuario.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').split()

    palabras_unicas = set(palabras)
    print("\nPalabras únicas:", palabras_unicas)

    conteo_palabras = {}
    for palabra in palabras:
        conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

    print("Conteo de palabras:", conteo_palabras)

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
def promedios_alumnos():
    alumnos_notas = {}
    print(" Ejercicio 6 ")
    for i in range(3):
        nombre_alumno = input(f"Ingresa el nombre del alumno {i+1}: ")
        notas = []
        for j in range(3):
            while True:
                try:
                    nota = float(input(f"Ingresa la nota {j+1} para {nombre_alumno}: "))
                    notas.append(nota)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número para la nota.")
        alumnos_notas[nombre_alumno] = tuple(notas)

    print("\nNotas de los alumnos:", alumnos_notas)
    print("\nPromedios de los alumnos:")
    for alumno, notas_tupla in alumnos_notas.items():
        if notas_tupla: 
            promedio = sum(notas_tupla) / len(notas_tupla)
            print(f"El promedio de {alumno} es: {promedio:.2f}")
        else:
            print(f"El alumno {alumno} no tiene notas para promediar.")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
def analizar_parciales():
    print(" Ejercicio 7 ")
    parcial1_aprobados = {101, 105, 110, 112, 115, 120}
    parcial2_aprobados = {101, 108, 112, 118, 120, 125}

    print("Estudiantes que aprobaron Parcial 1:", parcial1_aprobados)
    print("Estudiantes que aprobaron Parcial 2:", parcial2_aprobados)

    ambos_parciales = parcial1_aprobados.intersection(parcial2_aprobados)
    print("\nEstudiantes que aprobaron ambos parciales:", ambos_parciales)

    solo_uno = parcial1_aprobados.symmetric_difference(parcial2_aprobados)
    print("Estudiantes que aprobaron solo uno de los dos parciales:", solo_uno)

    total_aprobados = parcial1_aprobados.union(parcial2_aprobados)
    print("Estudiantes que aprobaron al menos un parcial:", total_aprobados)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.
def gestionar_stock():
    stock_productos = {
        "leche": 50,
        "pan": 30,
        "huevos": 120
    }
    print(" Ejercicio 8 ")
    print("Stock actual:", stock_productos)

    while True:
        print("\n Gestión de Stock ")
        print("1. Consultar stock de un producto")
        print("2. Agregar unidades / nuevo producto")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            producto_consulta = input("Ingresa el nombre del producto a consultar: ").lower()
            if producto_consulta in stock_productos:
                print(f"Stock de {producto_consulta}: {stock_productos[producto_consulta]} unidades.")
            else:
                print(f"El producto '{producto_consulta}' no existe en el stock.")
        elif opcion == '2':
            producto_modificar = input("Ingresa el nombre del producto: ").lower()
            try:
                cantidad = int(input(f"Ingresa la cantidad a agregar para '{producto_modificar}': "))
                if cantidad < 0:
                    print("La cantidad a agregar no puede ser negativa.")
                    continue
                
                if producto_modificar in stock_productos:
                    stock_productos[producto_modificar] += cantidad
                    print(f"Se agregaron {cantidad} unidades a '{producto_modificar}'. Nuevo stock: {stock_productos[producto_modificar]}.")
                else:
                    stock_productos[producto_modificar] = cantidad
                    print(f"Producto '{producto_modificar}' agregado con un stock inicial de {cantidad} unidades.")
            except ValueError:
                print("Cantidad inválida. Por favor, ingresa un número entero.")
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, selecciona 1, 2 o 3.")
    print("\nStock final:", stock_productos)

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.
def gestionar_agenda():
    agenda = {
        ("lunes", "09:00"): "Reunión de equipo",
        ("lunes", "14:00"): "Almuerzo con cliente",
        ("martes", "10:30"): "Presentación de proyecto",
        ("miercoles", "18:00"): "Clase de yoga"
    }
    print(" Ejercicio 9 ")
    print("Agenda actual:", agenda)

    print("\n Consultar Actividad en la Agenda ")
    dia_consulta = input("Ingresa el día (ej. lunes, martes): ").lower()
    hora_consulta = input("Ingresa la hora (ej. 09:00, 14:00): ")

    clave_consulta = (dia_consulta, hora_consulta)

    if clave_consulta in agenda:
        print(f"Actividad para {dia_consulta.capitalize()} a las {hora_consulta}: {agenda[clave_consulta]}")
    else:
        print(f"No hay actividad agendada para {dia_consulta.capitalize()} a las {hora_consulta}.")

# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
def invertir_diccionario_paises():
    print(" Ejercicio 10 ")
    paises_capitales = {
        "Argentina": "Buenos Aires",
        "España": "Madrid",
        "Francia": "París",
        "Italia": "Roma",
        "Alemania": "Berlín"
    }

    print("Diccionario original (País: Capital):", paises_capitales)

    capitales_paises = {}
    for pais, capital in paises_capitales.items():
        capitales_paises[capital] = pais

    print("Nuevo diccionario (Capital: País):", capitales_paises)



# Ejecución de los programas

if __name__ == "__main__":
    print("===== EJECUCIÓN DE PROGRAMAS =====")

    # Ejercicios 1, 2 y 3 (secuenciales, dependen del estado anterior)
    precios_frutas_base = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
    # Se llama a las funciones que encapsulan los ejercicios 1, 2 y 3.
    precios_despues_ej1 = ejecutar_ejercicio_1(precios_frutas_base)
    print("-" * 20)
    precios_despues_ej2 = ejecutar_ejercicio_2(precios_despues_ej1)
    print("-" * 20)
    ejecutar_ejercicio_3(precios_despues_ej2)
    print("-" * 20)

    # Llamadas a las funciones de los ejercicios restantes
    programa_telefonos()
    print("-" * 20)
    analizar_frase()
    print("-" * 20)
    promedios_alumnos()
    print("-" * 20)
    analizar_parciales()
    print("-" * 20)
    gestionar_stock()
    print("-" * 20)
    gestionar_agenda()
    print("-" * 20)
    invertir_diccionario_paises()
    print("-" * 20)

    print("===== FIN DE LA EJECUCIÓN =====")