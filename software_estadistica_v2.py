import statistics  # Importa el módulo statistics para realizar cálculos estadísticos.

# Funciones auxiliares
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

def convertir_datos(datos):
    datos_lista = datos.split(",")
    datos_convertidos = []
    for dato in datos_lista:
        if "." in dato:
            datos_convertidos.append(float(dato))
        else:
            datos_convertidos.append(int(dato))
    return datos_convertidos

def calcular_estadisticas(datos):
    n = len(datos)
    media = round(sum(datos) / n, 4)
    mediana = round(statistics.median(datos), 4)
    datos_inferiores = [n for n in datos if n < mediana]
    datos_superiores = [n for n in datos if n > mediana]
    cuartil1 = round(statistics.median(datos_inferiores), 4)
    cuartil3 = round(statistics.median(datos_superiores), 4)
    moda = statistics.multimode(datos)
    
    # Manejo de casos donde no hay moda
    if len(moda) == len(set(datos)):
        moda = "No hay moda"
    else:
        moda = ", ".join(map(str, moda))
    
    frec_abs = {}
    for dato in datos:
        if dato in frec_abs:
            frec_abs[dato] += 1
        else:
            frec_abs[dato] = 1

    frec_rel = {k: round(v / n, 4) for k, v in frec_abs.items()}
    frec_porcentual = {k: round(v * 100, 2) for k, v in frec_rel.items()}
    frec_abs_acum = {}
    contador = 0
    for k in frec_abs:
        contador += frec_abs[k]
        frec_abs_acum[k] = contador
    frec_rel_acum = {}
    contador = 0
    for k in frec_rel:
        contador += frec_rel[k]
        frec_rel_acum[k] = round(contador, 4)
    frec_porcentual_acum = {k: round(v * 100, 2) for k, v in frec_rel_acum.items()}
    
    varianza_muestral = sum((xi - media) ** 2 for xi in datos) / (n - 1)
    varianza_poblacional = sum((xi - media) ** 2 for xi in datos) / n
    desvio_muestral = round(varianza_muestral ** 0.5, 4)
    desvio_poblacional = round(varianza_poblacional ** 0.5, 4)
    
    return media, mediana, cuartil1, cuartil3, moda, desvio_muestral, desvio_poblacional

def calcular_frecuencias(datos):
    n = len(datos)
    datos.sort()
    frec_abs = {}
    for dato in datos:
        if dato in frec_abs:
            frec_abs[dato] += 1
        else:
            frec_abs[dato] = 1
    frec_rel = {k: round(v / n, 4) for k, v in frec_abs.items()}
    frec_porcentual = {k: round(v * 100, 2) for k, v in frec_rel.items()}
    frec_abs_acum = {}
    contador = 0
    for k in frec_abs:
        contador += frec_abs[k]
        frec_abs_acum[k] = contador
    frec_rel_acum = {}
    contador = 0
    for k in frec_rel:
        contador += frec_rel[k]
        frec_rel_acum[k] = round(contador, 4)
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
    print("2. Distribución Poisson (por implementar)")
    print("3. Distribución Hipergeométrica (por implementar)")
    print("4. Distribución Normal (por implementar)")
    print("5. Coeficiente de Curtosis (por implementar)")
    print("0. Volver al menú principal")

def obtener_datos():
    datos_entrada = input("Ingrese los datos separados por comas: ")
    return convertir_datos(datos_entrada)

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Seleccione una opción: ")
        if opcion_principal == "1":
            datos = obtener_datos()
            media, mediana, cuartil1, cuartil3, moda, desvio_muestral, desvio_poblacional = calcular_estadisticas(datos)
            frec_abs, frec_rel, frec_porcentual, frec_abs_acum, frec_rel_acum, frec_porcentual_acum = calcular_frecuencias(datos)
            
            while True:
                mostrar_menu_estadistica()
                opciones = input("Ingrese los números de las opciones que desea, separados por comas: ").split(',')
                for opcion in opciones:
                    if opcion == "1":
                        print(f"\nMedia: {media}")
                    elif opcion == "2":
                        print(f"\nMediana: {mediana}")
                    elif opcion == "3":
                        print(f"\nCuartil 1: {cuartil1}")
                    elif opcion == "4":
                        print(f"\nCuartil 3: {cuartil3}")
                    elif opcion == "5":
                        print(f"\nModa: {moda}")
                    elif opcion == "6":
                        print(f"\nFrecuencia Absoluta: {frec_abs}")
                    elif opcion == "7":
                        print(f"\nFrecuencia Absoluta Acumulada: {frec_abs_acum}")
                    elif opcion == "8":
                        print(f"\nFrecuencia Relativa: {frec_rel}")
                    elif opcion == "9":
                        print(f"\nFrecuencia Relativa Acumulada: {frec_rel_acum}")
                    elif opcion == "10":
                        print("\nFrecuencia Porcentual:")
                        for k, v in frec_porcentual.items():
                            print(f"{k}: {v}%")
                    elif opcion == "11":
                        print("\nFrecuencia Porcentual Acumulada:")
                        for k, v in frec_porcentual_acum.items():
                            print(f"{k}: {v}%")
                    elif opcion == "12":
                        print(f"\nDesvío Estándar Muestral: {desvio_muestral}")
                    elif opcion == "13":
                        print(f"\nDesvío Estándar Poblacional: {desvio_poblacional}")
                    elif opcion == "0":
                        break
                    else:
                        print(f"\nOpción {opcion} no válida. Por favor, intente de nuevo.")
                
                otra_consulta = input("\n¿Desea realizar otra consulta en Estadística Descriptiva? (si/no): ")
                if otra_consulta.lower() != 'si':
                    break

        elif opcion_principal == "2":
            while True:
                mostrar_menu_probabilidad()
                opcion_probabilidad = input("Seleccione una opción: ")
                
                if opcion_probabilidad == "1":
                    n = int(input("\nIngrese número de ensayos (n): "))
                    p = float(input("Ingrese probabilidad de éxito (p): "))
                    k = int(input("Ingrese número de éxitos deseados (k): "))
                    
                    print("\nSeleccione el tipo de cálculo:")
                    print("1. P(X = k)")
                    print("2. P(X < k)")
                    print("3. P(X ≤ k)")
                    print("4. P(X > k)")
                    print("5. P(X ≥ k)")
                    tipo_calculo = int(input("Ingrese el tipo de cálculo: "))
                    
                    probabilidad, porcentaje = calcular_probabilidades_binomial(n, p, k, tipo_calculo)
                    
                    print(f"\nLa probabilidad es: {probabilidad} ({porcentaje}%)")
                
                elif opcion_probabilidad in ["2", "3", "4", "5"]:
                    print("\nEsta funcionalidad está en desarrollo.")
                
                elif opcion_probabilidad == "0":
                    break
                
                else:
                    print(f"\nOpción {opcion_probabilidad} no válida. Por favor, intente de nuevo.")
                
                otra_consulta = input("\n¿Desea realizar otra consulta en Probabilidad? (si/no): ")
                if otra_consulta.lower() != 'si':
                    break

        elif opcion_principal == "0":
            print("\nSaliendo del programa...")
            break

        else:
            print(f"\nOpción {opcion_principal} no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
