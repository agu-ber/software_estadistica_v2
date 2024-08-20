import statistics  # Importa el módulo statistics para realizar cálculos estadísticos.

# Constante de Euler con 20 decimales
EULER = 2.71828182845904523536

# Funciones auxiliares para probabilidades
def factorial(x):
    resultado = 1
    for i in range(2, x + 1):
        resultado = resultado * i
    return resultado

def coeficiente_binomial(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def formula_binomial(n, k, p):
    coeficiente = coeficiente_binomial(n, k)
    distribucion_binomial = coeficiente * (p ** k) * ((1 - p) ** (n - k))
    return round(distribucion_binomial, 4)

def formula_poisson(x, u):
    distribucion_poisson = ((EULER ** -u) * (u**x)) / factorial(x)
    return round(distribucion_poisson, 4)

# Cálculos para probabilidades de la distribución binomial
def calcular_probabilidades_binomial(n, p, k, tipo_calculo):
    if tipo_calculo == 1:  # P(X = k)
        probabilidad = formula_binomial(n, k, p)
    elif tipo_calculo == 2:  # P(X < k)
        probabilidad = sum(formula_binomial(n, i, p) for i in range(k))
    elif tipo_calculo == 3:  # P(X ≤ k)
        probabilidad = sum(formula_binomial(n, i, p) for i in range(k + 1))
    elif tipo_calculo == 4:  # P(X > k)
        probabilidad = sum(formula_binomial(n, i, p) for i in range(k + 1, n + 1))
    elif tipo_calculo == 5:  # P(X ≥ k)
        probabilidad = sum(formula_binomial(n, i, p) for i in range(k, n + 1))

    return round(probabilidad, 4), round(probabilidad * 100, 2)  # Retorna en decimal y porcentaje.

# Cálculos para probabilidades de la distribución Poisson
def calcular_probabilidades_poisson(x, u, tipo_calculo):
    if tipo_calculo == 1:  # P(X = k)
        probabilidad = formula_poisson(x, u)
    elif tipo_calculo == 2:  # P(X < k)
        probabilidad = sum(formula_poisson(i, u) for i in range(x))
    elif tipo_calculo == 3:  # P(X ≤ k)
        probabilidad = sum(formula_poisson(i, u) for i in range(x + 1))
    elif tipo_calculo == 4:  # P(X > k)
        probabilidad = sum(formula_poisson(i, u) for i in range(x + 1, int(u * 10)))  # Rango ampliado
    elif tipo_calculo == 5:  # P(X ≥ k)
        probabilidad = sum(formula_poisson(i, u) for i in range(x, int(u * 10)))  # Rango ampliado

    return round(probabilidad, 4), round(probabilidad * 100, 2)  # Retorna en decimal y porcentaje.

def convertir_datos(datos):
    datos_lista = datos.split(",")  # Divide la cadena en una lista donde cada elemento es se separa por una coma.
    datos_convertidos = []  # Definimos una lista vacía donde se van a guardar los datos.
    for dato in datos_lista:  # Ciclo for para que itere sobre cada dato en la lista de datos ingresados en línea 1.
        if "." in dato:  # Si el dato contiene un punto, se considera decimal.
            datos_convertidos.append(float(dato))  # Convierte a float y lo agrega a la lista.
        else:
            datos_convertidos.append(int(dato))  # Si no, convierte a entero y lo agrega a la lista.
    return datos_convertidos  # Retorna la lista de datos ya convertidos como una lista nueva.

def calcular_estadisticas(datos):
    n = len(datos)  # Calcula cantidad de datos.
    media = round(sum(datos) / n, 4)  # Calcula la media con 4 decimales.
    mediana = round(statistics.median(datos), 4)  # Calcula la mediana con 4 decimales.
    
    datos_inferiores = [n for n in datos if n < mediana]  # Filtra los datos inferiores a la mediana.
    datos_superiores = [n for n in datos if n > mediana]  # Filtra los datos superiores a la mediana.
    cuartil1 = round(statistics.median(datos_inferiores), 4)  # Calcula el primer cuartil con 4 decimales.
    cuartil3 = round(statistics.median(datos_superiores), 4)  # Calcula el tercer cuartil con 4 decimales.
    moda = statistics.multimode(datos)  # Calcula la moda.

    # Si hay más de una moda, calcular la frecuencia de cada una
    frecuencias_moda = {}
    if len(moda) > 1:
        for m in moda:
            frecuencias_moda[m] = datos.count(m)
    else:
        frecuencias_moda[moda[0]] = datos.count(moda[0])

    varianza_muestral = sum((xi - media) ** 2 for xi in datos) / (n - 1)  # Calcula la varianza muestral.
    varianza_poblacional = sum((xi - media) ** 2 for xi in datos) / n  # Calcula la varianza poblacional.
    desvio_muestral = round(varianza_muestral ** 0.5, 4)  # Calcula el desvío estándar muestral con 4 decimales.
    desvio_poblacional = round(varianza_poblacional ** 0.5, 4)  # Calcula el desvío estándar poblacional con 4 decimales.
    
    return media, mediana, cuartil1, cuartil3, moda, frecuencias_moda, desvio_muestral, desvio_poblacional  # Retorna cada cálculo previo.

def calcular_frecuencias(datos):
    n = len(datos)
    datos.sort()  # Ordena los datos.

    # Frecuencia Absoluta:
    frec_abs = {}  # Definimos un diccionario vacío para la frecuencia absoluta.
    for dato in datos:
        if dato in frec_abs:
            frec_abs[dato] += 1  # Incrementa el contador si el dato está en el diccionario.
        else:
            frec_abs[dato] = 1  # Inicializa el contador si el dato no está en el diccionario.

    # Frecuencia Relativa:
    frec_rel = {k: round(v / n, 4) for k, v in frec_abs.items()}

    # Frecuencia Porcentual:
    frec_porcentual = {k: round(v * 100, 2) for k, v in frec_rel.items()}

    # Frecuencia Absoluta Acumulada:
    frec_abs_acum = {}
    contador = 0
    for k in frec_abs:
        contador += frec_abs[k]
        frec_abs_acum[k] = contador

    # Frecuencia Relativa Acumulada:
    frec_rel_acum = {}
    contador = 0
    for k in frec_rel:
        contador += frec_rel[k]
        frec_rel_acum[k] = round(contador, 4)

    # Frecuencia Porcentual Acumulada:
    frec_porcentual_acum = {k: round(v * 100, 2) for k, v in frec_rel_acum.items()}

    return frec_abs, frec_rel, frec_porcentual, frec_abs_acum, frec_rel_acum, frec_porcentual_acum

def mostrar_menu_principal():
    print("\nMenú principal:")
    print("1. Estadística Descriptiva")
    print("2. Probabilidad")
    print("0. Salir")

def mostrar_menu_estadistica():
    print("\nMenú de Estadística Descriptiva:")
    print("1. Media")
    print("2. Mediana")
    print("3. Cuartil 1")
    print("4. Cuartil 3")
    print("5. Moda")
    print("6. Frecuencia Absoluta")
    print("7. Frecuencia Absoluta Acumulada")
    print("8. Frecuencia Relativa")
    print("9. Frecuencia Relativa Acumulada")
    print("10. Frecuencia Porcentual")
    print("11. Frecuencia Porcentual Acumulada")
    print("12. Desvío Estándar Muestral")
    print("13. Desvío Estándar Poblacional")
    print("0. Volver al menú principal")

def mostrar_menu_probabilidad():
    print("\nMenú de Probabilidad:")
    print("1. Distribución Binomial")
    print("2. Distribución Poisson")
    print("0. Volver al menú principal")

def mostrar_menu_probabilidad_binomial():
    print("\nCálculo de Distribución Binomial:")
    print("1. P(X = k)")
    print("2. P(X < k)")
    print("3. P(X ≤ k)")
    print("4. P(X > k)")
    print("5. P(X ≥ k)")
    print("0. Volver al menú de probabilidad")

def mostrar_menu_probabilidad_poisson():
    print("\nCálculo de Distribución Poisson:")
    print("1. P(X = k)")
    print("2. P(X < k)")
    print("3. P(X ≤ k)")
    print("4. P(X > k)")
    print("5. P(X ≥ k)")
    print("0. Volver al menú de probabilidad")

def mostrar_resultados_estadistica(media, mediana, cuartil1, cuartil3, moda, frecuencias_moda, desvio_muestral, desvio_poblacional):
    print("\nResultados:")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Cuartil 1: {cuartil1}")
    print(f"Cuartil 3: {cuartil3}")
    print(f"Moda: {moda}")
    if len(frecuencias_moda) > 1:
        print("Frecuencias de las modas:")
        for m, freq in frecuencias_moda.items():
            print(f"Moda: {m}, Frecuencia: {freq}")
    else:
        print(f"Frecuencia de la moda: {list(frecuencias_moda.values())[0]}")
    print(f"Desvío Estándar Muestral: {desvio_muestral}")
    print(f"Desvío Estándar Poblacional: {desvio_poblacional}")

def ejecutar_estadistica_descriptiva():
    datos = input("Ingrese los datos separados por comas (ej. 1,2,3,4): ")
    datos_convertidos = convertir_datos(datos)

    media, mediana, cuartil1, cuartil3, moda, frecuencias_moda, desvio_muestral, desvio_poblacional = calcular_estadisticas(datos_convertidos)
    frec_abs, frec_rel, frec_porcentual, frec_abs_acum, frec_rel_acum, frec_porcentual_acum = calcular_frecuencias(datos_convertidos)

    while True:
        mostrar_menu_estadistica()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            print(f"\nLa media es: {media}")
        elif opcion == 2:
            print(f"\nLa mediana es: {mediana}")
        elif opcion == 3:
            print(f"\nEl cuartil 1 es: {cuartil1}")
        elif opcion == 4:
            print(f"\nEl cuartil 3 es: {cuartil3}")
        elif opcion == 5:
            print(f"\nLa moda es: {moda}")
            if len(frecuencias_moda) > 1:
                print("Frecuencias de las modas:")
                for m, freq in frecuencias_moda.items():
                    print(f"Moda: {m}, Frecuencia: {freq}")
            else:
                print(f"Frecuencia de la moda: {list(frecuencias_moda.values())[0]}")
        elif opcion == 6:
            print(f"\nFrecuencia Absoluta: {frec_abs}")
        elif opcion == 7:
            print(f"\nFrecuencia Absoluta Acumulada: {frec_abs_acum}")
        elif opcion == 8:
            print(f"\nFrecuencia Relativa: {frec_rel}")
        elif opcion == 9:
            print(f"\nFrecuencia Relativa Acumulada: {frec_rel_acum}")
        elif opcion == 10:
            print(f"\nFrecuencia Porcentual: {frec_porcentual}")
        elif opcion == 11:
            print(f"\nFrecuencia Porcentual Acumulada: {frec_porcentual_acum}")
        elif opcion == 12:
            print(f"\nEl Desvío Estándar Muestral es: {desvio_muestral}")
        elif opcion == 13:
            print(f"\nEl Desvío Estándar Poblacional es: {desvio_poblacional}")
        elif opcion == 0:
            break

        continuar = input("\n¿Desea realizar otro cálculo de estadística descriptiva? (s/n): ").lower()
        if continuar != 's':
            break

def ejecutar_probabilidad():
    while True:
        mostrar_menu_probabilidad()
        opcion_probabilidad = int(input("Seleccione una opción: "))

        if opcion_probabilidad == 1:
            n = int(input("Ingrese el número de ensayos (n): "))
            p = float(input("Ingrese la probabilidad de éxito en cada ensayo (p): "))
            k = int(input("Ingrese el número de éxitos deseados (k): "))

            while True:
                mostrar_menu_probabilidad_binomial()
                opcion_binomial = int(input("Seleccione una opción: "))

                if opcion_binomial == 0:
                    break

                probabilidad_decimal, probabilidad_porcentaje = calcular_probabilidades_binomial(n, p, k, opcion_binomial)
                print(f"\nProbabilidad: {probabilidad_decimal} ({probabilidad_porcentaje}%)")

                continuar = input("\n¿Desea realizar otro cálculo con la distribución binomial? (s/n): ").lower()
                if continuar != 's':
                    break

        elif opcion_probabilidad == 2:
            x = int(input("Ingrese el número de ocurrencias (x): "))
            u = float(input("Ingrese el número promedio de ocurrencias o esperanza (λ): "))

            while True:
                mostrar_menu_probabilidad_poisson()
                opcion_poisson = int(input("Seleccione una opción: "))

                if opcion_poisson == 0:
                    break

                probabilidad_decimal, probabilidad_porcentaje = calcular_probabilidades_poisson(x, u, opcion_poisson)
                print(f"\nProbabilidad: {probabilidad_decimal} ({probabilidad_porcentaje}%)")

                continuar = input("\n¿Desea realizar otro cálculo con la distribución Poisson? (s/n): ").lower()
                if continuar != 's':
                    break

        elif opcion_probabilidad == 0:
            break

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = int(input("Seleccione una opción: "))

        if opcion_principal == 1:
            ejecutar_estadistica_descriptiva()
        elif opcion_principal == 2:
            ejecutar_probabilidad()
        elif opcion_principal == 0:
            print("¡Gracias por utilizar el programa!")
            break

if __name__ == "__main__":
    main()
