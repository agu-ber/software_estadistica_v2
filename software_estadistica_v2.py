import statistics  # Importa el módulo statistics para realizar cálculos estadísticos.
from tabla_z import tabla_z # Importa la tabla Z

# Constante de Euler con 20 decimales
EULER = 2.71828182845904523536

# Funciones auxiliares para probabilidades
def factorial(x):
    # Calcula el factorial de un número dado 'x'.
    # Si 'x' es 0, retorna 1 porque 0! es 1 por definición.
    if x == 0:
        return 1
    resultado = 1
    # Calcula el producto de todos los enteros positivos desde 2 hasta 'x'.
    for i in range(2, x + 1):
        resultado = resultado * i
    # Retorna el resultado del factorial.
    return resultado

def coeficiente_binomial(n, k):
    # Calcula el coeficiente binomial (también conocido como "número combinatorio") para dos números dados 'n' y 'k'.
    # Esto representa la cantidad de formas en que se pueden elegir 'k' elementos de un conjunto de 'n' elementos.
    # Usa la fórmula: n! / (k! * (n-k)!)
    return factorial(n) // (factorial(k) * factorial(n - k))

def formula_binomial(n, p, k):
    # Calcula la probabilidad de obtener exactamente 'k' éxitos en 'n' ensayos independientes,
    # cada uno con una probabilidad de éxito 'p', usando la distribución binomial.
    # Obtiene el coeficiente binomial usando la función 'coeficiente_binomial(n, k)'.
    coeficiente = coeficiente_binomial(n, k)
    # Aplica la fórmula de la distribución binomial: coeficiente * p^k * (1-p)^(n-k)
    distribucion_binomial = coeficiente * (p ** k) * ((1 - p) ** (n - k))
    # Redondea el resultado a cuatro decimales y lo retorna.
    return round(distribucion_binomial, 4)

def formula_poisson(u, k):
    # Calcula la probabilidad de obtener exactamente 'k' ocurrencias en un intervalo dado
    # según la distribución de Poisson, donde 'u' es el número promedio de ocurrencias (λ).
    # Utiliza la fórmula de Poisson: (e^(-λ) * λ^k) / k!
    distribucion_poisson = ((EULER ** -u) * (u**k)) / factorial(k)
    # Redondea el resultado a cuatro decimales y lo retorna.
    return round(distribucion_poisson, 4)

def formula_hipergeometrica(M, k, n, N):
    # Calcula la probabilidad de obtener exactamente 'k' éxitos en una muestra de tamaño 'n'
    # extraída de una población de tamaño 'N' que contiene 'M' éxitos, sin reemplazo.
    # Utiliza la fórmula de la distribución hipergeométrica.

    # Calcula el coeficiente combinatorio de elegir 'k' éxitos de 'M' éxitos totales.
    coeficiente1 = coeficiente_binomial(M, k) 
    # Calcula el coeficiente combinatorio de elegir 'n-k' fracasos del total de fracasos (N-M).
    coeficiente2 = coeficiente_binomial(N-M, n-k)
    # Calcula el coeficiente combinatorio de elegir 'n' elementos de 'N' elementos totales.
    coeficiente3 = coeficiente_binomial(N, n)
    # Calcula la probabilidad hipergeométrica utilizando la combinación de los coeficientes.
    distribucion_hipergeometrico = (coeficiente1 * coeficiente2) / coeficiente3
    # Redondea el resultado a cuatro decimales y lo retorna.
    return round(distribucion_hipergeometrico, 4)

def estandarizar(m, s, x):
    # Calcula el valor Z para una distribución normal estandarizada.
    # 'm' es la media, 's' es la desviación estándar, y 'x' es el valor de interés.
    # La fórmula de estandarización es: Z = (x - μ) / σ
    valor_z = (x - m) / s
    # Retorna el valor estandarizado (Z).
    return valor_z

def buscar_probabilidad_z(z):
    # Busca la probabilidad acumulada para un valor Z en una tabla de distribución normal estándar.
    # 'z' es el valor Z que se busca.

    probabilidad = 0 # Inicializa la probabilidad.

    if z < -4:
        # Si 'z' es menor que -4, la probabilidad es prácticamente 0.
        probabilidad = 0
    elif z > 4:
        # Si 'z' es mayor que 4, la probabilidad es prácticamente 1.
        probabilidad = 1
    elif z in tabla_z:
        # Si 'z' está en la tabla de valores Z precalculados, usa el valor correspondiente.
        probabilidad = tabla_z[z]
    else:
        # Si 'z' no está en la tabla, interpola entre los valores más cercanos para estimar la probabilidad.
        lower_z = max(key for key in tabla_z if key < z) # Encuentra el valor Z más cercano por debajo de 'z'.
        upper_z = min(key for key in tabla_z if key > z) # Encuentra el valor Z más cercano por encima de 'z'.
        lower_p = tabla_z[lower_z] # Probabilidad acumulada correspondiente al valor Z inferior.
        upper_p = tabla_z[upper_z] # Probabilidad acumulada correspondiente al valor Z superior.
        # Promedia las probabilidades de los valores más cercanos para aproximar la probabilidad de 'z'.
        probabilidad = (lower_p + upper_p) / 2 

    # Retorna la probabilidad calculada.
    return probabilidad

# Cálculos para probabilidades de la distribución binomial
def calcular_probabilidades_binomial(n, p, k, tipo_calculo):
    # Calcula la probabilidad de eventos usando la distribución binomial.
    # 'n' es el número de ensayos, 'p' es la probabilidad de éxito en cada ensayo,
    # 'k' es el número de éxitos de interés, y 'tipo_calculo' define el tipo de probabilidad a calcular.
    
    if tipo_calculo == 1:  # P(X = k)
        # Probabilidad de exactamente 'k' éxitos.
        probabilidad = formula_binomial(n, p, k)
        prob_string = f"P(X = {k})"
    elif tipo_calculo == 2:  # P(X < k)
        # Probabilidad de menos de 'k' éxitos.
        probabilidad = sum(formula_binomial(n, p, i) for i in range(k))
        prob_string = f"P(X < {k})"
    elif tipo_calculo == 3:  # P(X ≤ k)
        # Probabilidad de 'k' o menos éxitos.
        probabilidad = sum(formula_binomial(n, p, i) for i in range(k + 1))
        prob_string = f"P(X ≤ {k})"
    elif tipo_calculo == 4:  # P(X > k)
        # Probabilidad de más de 'k' éxitos.
        probabilidad = sum(formula_binomial(n, p, i) for i in range(k + 1, n + 1))
        prob_string = f"P(X > {k})"
    elif tipo_calculo == 5:  # P(X ≥ k)
        # Probabilidad de 'k' o más éxitos.
        probabilidad = sum(formula_binomial(n, p, i) for i in range(k, n + 1))
        prob_string = f"P(X ≥ {k})"

    # Retorna la probabilidad redondeada a cuatro decimales, su valor en porcentaje y el tipo de cálculo realizado.
    return round(probabilidad, 4), round(probabilidad * 100, 2), prob_string  # Retorna en decimal y porcentaje.

# Cálculos para probabilidades de la distribución Poisson
def calcular_probabilidades_poisson(u, k, tipo_calculo):
    # Calcula la probabilidad de eventos usando la distribución de Poisson.
    # 'u' es el número medio de ocurrencias en un intervalo, 'k' es el número de ocurrencias de interés,
    # y 'tipo_calculo' define el tipo de probabilidad a calcular.

    if tipo_calculo == 1:  # P(X = k)
        # Probabilidad de exactamente 'k' éxitos.
        probabilidad = formula_poisson(u, k)
        prob_string = f"P(X = {k})"
    elif tipo_calculo == 2:  # P(X < k)
        # Probabilidad de menos de 'k' éxitos.
        probabilidad = sum(formula_poisson(u, i) for i in range(k))
        prob_string = f"P(X < {k})"
    elif tipo_calculo == 3:  # P(X ≤ k)
        # Probabilidad de 'k' o menos éxitos.
        probabilidad = sum(formula_poisson(u, i) for i in range(k + 1))
        prob_string = f"P(X ≤ {k})"
    elif tipo_calculo == 4:  # P(X > k)
        # Probabilidad de más de 'k' éxitos. Se amplía el rango de cálculo.
        probabilidad = sum(formula_poisson(u, i) for i in range(k + 1, int(u * 10)))  # Rango ampliado
        prob_string = f"P(X > {k})"
    elif tipo_calculo == 5:  # P(X ≥ k)
        # Probabilidad de 'k' o más éxitos. Se amplía el rango de cálculo.
        probabilidad = sum(formula_poisson(u, i) for i in range(k, int(u * 10)))  # Rango ampliado
        prob_string = f"P(X ≥ {k})"

    # Retorna la probabilidad redondeada a cuatro decimales, su valor en porcentaje y el tipo de cálculo realizado.
    return round(probabilidad, 4), round(probabilidad * 100, 2), prob_string  # Retorna en decimal y porcentaje.

# Cálculos para probabilidades de la distribución hipergeométrica
def calcular_probabilidades_hipergeometrica(M, k, n, N, tipo_calculo):
    # Calcula la probabilidad de eventos usando la distribución hipergeométrica.
    # 'M' es el número total de éxitos en la población, 'k' es el número de éxitos deseados,
    # 'n' es el tamaño de la muestra, 'N' es el tamaño de la población, y 'tipo_calculo' define el tipo de probabilidad a calcular.

    if tipo_calculo == 1: # P(X = k)
        # Probabilidad de exactamente 'k' éxitos.
        probabilidad = formula_hipergeometrica(M, k, n, N)
        prob_string = f"P(X = {k})"
    elif tipo_calculo == 2: # P(X < k)
        # Probabilidad de menos de 'k' éxitos.
        probabilidad = sum(formula_hipergeometrica(M, i, n, N) for i in range(k))
        prob_string = f"P(X < {k})"
    elif tipo_calculo == 3: # P(X ≤ k)
        # Probabilidad de 'k' o menos éxitos.
        probabilidad = sum(formula_hipergeometrica(M, i, n, N) for i in range(k + 1))
        prob_string = f"P(X ≤ {k})"
    elif tipo_calculo == 4: # P(X > k)
        # Probabilidad de más de 'k' éxitos. Calcula el mínimo entre 'n' (tamaño de la muestra) y 'M' (número de éxitos en la población).
        probabilidad = sum(formula_hipergeometrica(M, i, n, N) for i in range(k + 1, min(n, M))) # Se calcula el mínimo entre el tamaño de la muestra y el número de éxitos en la población
        prob_string = f"P(X > {k})"
    elif tipo_calculo == 5: # P(X ≥ k)
        # Probabilidad de 'k' o más éxitos. Calcula el mínimo entre 'n' y 'M'.
        probabilidad = sum(formula_hipergeometrica(M, i, n, N) for i in range(k, min(n, M)))
        prob_string = f"P(X ≥ {k})"

    # Retorna la probabilidad redondeada a cuatro decimales, su valor en porcentaje y el tipo de cálculo realizado.
    return round(probabilidad, 4), round(probabilidad * 100, 2), prob_string

# Cálculos de las probabilidades para la distribución normal
def calcular_probabilidad_distribucion_normal(m, s, datos_x, tipo_probabilidad):
    # Calcula la probabilidad de eventos usando la distribución normal.
    # 'm' es la media de la distribución, 's' es la desviación estándar,
    # 'datos_x' son los valores a evaluar, y 'tipo_probabilidad' define el tipo de probabilidad a calcular.

    # Calcula los valores Z correspondientes a los datos de entrada.
    z_values = [estandarizar(m, s, x) for x in datos_x]
    # Busca las probabilidades acumuladas correspondientes a cada valor Z.
    resultados = [buscar_probabilidad_z(z) for z in z_values]

    if tipo_probabilidad == 1:  # P(x > a)
        # Probabilidad de que el valor sea mayor que 'a'.
        probabilidad = 1 - resultados[0]
        prob_string = f"P(X > {datos_x[0]})"
    elif tipo_probabilidad == 2:  # P(x < a)
        # Probabilidad de que el valor sea menor que 'a'.
        probabilidad = resultados[0]
        prob_string = f"P(X < {datos_x[0]})"
    elif tipo_probabilidad == 3:  # P(a < x < b)
        # Probabilidad de que el valor esté entre 'a' y 'b'.
        probabilidad = resultados[1] - resultados[0]
        prob_string = f"P({datos_x[0]} < X < {datos_x[1]})"
    elif tipo_probabilidad == 4:  # P(x < a or x > b)
        # Probabilidad de que el valor esté fuera del rango [a, b].
        probabilidad = resultados[0] + (1 - resultados[1])
        prob_string = f"P(X < {datos_x[0]} o X > {datos_x[1]})"

    # Retorna la probabilidad redondeada a cuatro decimales, su valor en porcentaje, el tipo de cálculo realizado y los valores Z utilizados.
    return round(probabilidad, 4), round(probabilidad * 100, 2), prob_string, z_values

# Dividir datos ingresados
def convertir_datos(datos):
    datos_lista = datos.split(",")  # Divide la cadena en una lista donde cada elemento es se separa por una coma.
    datos_convertidos = []  # Definimos una lista vacía donde se van a guardar los datos.
    for dato in datos_lista:  # Ciclo for para que itere sobre cada dato en la lista de datos ingresados en línea 1.
        if "." in dato:  # Si el dato contiene un punto, se considera decimal.
            datos_convertidos.append(float(dato))  # Convierte a float y lo agrega a la lista.
        else:
            datos_convertidos.append(int(dato))  # Si no, convierte a entero y lo agrega a la lista.
    return datos_convertidos  # Retorna la lista de datos ya convertidos como una lista nueva.

# Calculos de estadística descriptiva
def calcular_estadisticas(datos):
    n = len(datos)  # Calcula cantidad de datos.
    media = round(sum(datos) / n, 4)  # Calcula la media con 4 decimales.
    mediana = round(statistics.median(datos), 4)  # Calcula la mediana con 4 decimales.
    
    datos_inferiores = [n for n in datos if n < mediana]  # Filtra los datos inferiores a la mediana.
    datos_superiores = [n for n in datos if n > mediana]  # Filtra los datos superiores a la mediana.
    cuartil1 = round(statistics.median(datos_inferiores), 4)  # Calcula el primer cuartil con 4 decimales.
    cuartil3 = round(statistics.median(datos_superiores), 4)  # Calcula el tercer cuartil con 4 decimales.
    moda = statistics.multimode(datos)  # Calcula la moda.

    # Calcular frecuencias de cada valor
    frecuencias = {valor: datos.count(valor) for valor in set(datos)}
    frecuencia_max = max(frecuencias.values())
    
    # Verificar si todos los valores tienen la misma frecuencia
    if all(frecuencia == frecuencia_max for frecuencia in frecuencias.values()):
        moda = "No hay moda"
        frecuencias_moda = {"Todos los valores tienen frecuencia": frecuencia_max}
    else:
        # Si hay más de una moda, mostrar la frecuencia solo una vez
        frecuencias_moda = {}
        if len(moda) > 1:
            for m in moda:
                frecuencias_moda[m] = frecuencia_max
        else:
            frecuencias_moda[moda[0]] = frecuencia_max

    varianza_muestral = sum((xi - media) ** 2 for xi in datos) / (n - 1)  # Calcula la varianza muestral.
    varianza_poblacional = sum((xi - media) ** 2 for xi in datos) / n  # Calcula la varianza poblacional.
    desvio_muestral = round(varianza_muestral ** 0.5, 4)  # Calcula el desvío estándar muestral con 4 decimales.
    desvio_poblacional = round(varianza_poblacional ** 0.5, 4)  # Calcula el desvío estándar poblacional con 4 decimales.
    cuarto_momento = sum((xi - media) ** 4 for xi in datos) / n
    curtosis = round(cuarto_momento / (desvio_poblacional ** 4) - 3, 4)

    return media, mediana, cuartil1, cuartil3, moda, frecuencias_moda, desvio_muestral, desvio_poblacional, curtosis  # Retorna cada cálculo previo.

def calcular_frecuencias(datos):
    n = len(datos) 
    datos.sort()  # Ordena los datos.

    # Frecuencia Absoluta:
    # Número de veces en que aparece repetido un mismo valor de la variable
    frec_abs = {}  #Definimos un diccionario vacio para la frecuencia absoluta.
    for dato in datos:
        if dato in frec_abs:
            frec_abs[dato] += 1  # Incrementa el contador si el dato esta en el diccionario.
        else:
            frec_abs[dato] = 1  # Inicializa el contador si el dato no está en el diccionario.

    # Frecuencia Relativa:
    # Es el cociente entre su frecuencia absoluta y la suma de todas las frecuencias absolutas.
    frec_rel = {}
    for k, v in frec_abs.items():
        frec_rel[k] = round(v / n, 4)  # Calcula la frecuencia relativa.

    # Frecuencia porcentual
    # Es igual a la frecuencia relativa multiplicada por 100. 
    # Expresa el porcentaje que el valor de una variable tiene en el total de observaciones.
    frec_porcentual = {}
    for k, v in frec_rel.items():
        frec_porcentual[k] = round(v * 100, 2) # Calcula la frecuencia porcentual.

    # Frecuencia absoluta acumulada
    # Se obtiene sumando todas las frecuencias absolutas de las variables que le anteceden más la frecuencia absoluta de dicha variable.
    frec_abs_acum = {}  #Definimos un diccionario vacio para la frecuencia absoluta acumulada.
    contador = 0
    for k in frec_abs:
        contador += frec_abs[k]  # Acumula las frecuencias absolutas.
        frec_abs_acum[k] = contador  # Asigna la frecuencia acumulada al dato.

    # Frecuencia relativa acumulada
    # Se obtiene sumando todas las frecuencias relativas que la anteceden más la frecuencia relativa de dicha variable.
    frec_rel_acum = {}  #Definimos un diccionario vacio para la frecuencia relativa acumulada.
    contador = 0
    for k in frec_rel:
        contador += frec_rel[k]  # Acumula las frecuencias relativas.
        frec_rel_acum[k] = round(contador, 4)  # Asigna la frecuencia relativa acumulada al dato.

    # Frecuencia porcentual acumulada
    # Se obtiene sumando todas las frecuencias porcentuales de las variables que la anteceden
    # más la frecuencia porcentual de dicha variable.

    frec_porcentual_acum = {}
    for k, v in frec_rel_acum.items():
        frec_porcentual_acum[k] = round(v * 100, 2) # Calcula la frecuencia porcentual acumulada.
    
    return frec_abs, frec_rel, frec_porcentual, frec_abs_acum, frec_rel_acum, frec_porcentual_acum  # Retorna todas las frecuencias calculadas.

# Funciones para los menús
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
    print("14. Coeficiente de Curtosis")
    print("0. Volver al menú principal")

def mostrar_menu_probabilidad():
    print("\nMenú de Probabilidad:")
    print("1. Distribución Binomial")
    print("2. Distribución Poisson")
    print("3. Distribución Hipergeométrica")
    print("4. Distribución Normal")
    print("0. Volver al menú principal")

def mostrar_menu_probabilidad_especifica(tipo_distribucion):
    if tipo_distribucion in ['binomial', 'poisson', 'hipergeometrica']: 
        if tipo_distribucion == 'binomial':
            print("\nCálculo de Distribución Binomial:")
        elif tipo_distribucion == 'poisson':
            print("\nCálculo de Distribución Poisson:")
        elif tipo_distribucion == 'hipergeometrica':
            print("\nCálculo de Distribución Hipergeométrica:")

        print("1. P(X = k)")
        print("2. P(X < k)")
        print("3. P(X ≤ k)")
        print("4. P(X > k)")
        print("5. P(X ≥ k)")
    
    elif tipo_distribucion == 'normal':
        print("\nCálculo de Distribución Normal:")
        print("1. P(X > a)")
        print("2. P(X < a)")
        print("3. P(a < X < b)")
        print("4. P(X < a o X > b)")

    print("0. Volver al menú de probabilidad")

# Validaciones para los inputs
def obtener_opciones_estadistica():
    """
    Solicita al usuario que ingrese una o más opciones para el cálculo de estadísticas y valida la entrada.

    :return: Lista de opciones seleccionadas por el usuario que son válidas.
    """
    while True:
        opciones = input("Seleccione una o más opciones separadas por comas (ej. 1,2,5): ").split(',')
        opciones_validas = True
        opciones_limpias = []
        
        for opcion in opciones:
            opcion = opcion.strip() # Remueve espacios en blanco alrededor de la entrada
            if opcion.isdigit() and 0 <= int(opcion) <= 14: # Verifica que la entrada sea un número entre 0 y 14
                opciones_limpias.append(opcion) # Agrega la opción válida a la lista
            else:
                print(f"Opción '{opcion}' no válida. Intente de nuevo.")
                opciones_validas = False # Indica que hubo una opción no válida
        
        if opciones_validas:
            return opciones_limpias # Devuelve la lista de opciones si todas son válidas
        
def obtener_opcion_valida(mensaje, opciones_validas):
    """
    Solicita al usuario que ingrese una opción y valida que esté en el rango de opciones válidas.

    :param mensaje: El mensaje que se muestra al usuario para solicitar la opción.
    :param opciones_validas: Lista de opciones válidas que el usuario puede ingresar.
    :return: La opción seleccionada por el usuario que es válida.
    """
    while True:
        try:
            opcion = int(input(mensaje))
            if opcion in opciones_validas:
                return opcion
            else:
                print(f"Por favor, seleccione una opción válida ({', '.join(map(str, opciones_validas))}).")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")                        

# Ejecución de menús

def ejecutar_estadistica_descriptiva():
    datos = input("Ingrese los datos separados por comas (ej. 1,2,3,4): ")
    datos_convertidos = convertir_datos(datos)

    media, mediana, cuartil1, cuartil3, moda, frecuencias_moda, desvio_muestral, desvio_poblacional, curtosis = calcular_estadisticas(datos_convertidos)
    frec_abs, frec_rel, frec_porcentual, frec_abs_acum, frec_rel_acum, frec_porcentual_acum = calcular_frecuencias(datos_convertidos)

    while True:
        mostrar_menu_estadistica()
        opciones = obtener_opciones_estadistica()

        for opcion_estadistica in opciones:
            opcion_estadistica = opcion_estadistica.strip()
            if opcion_estadistica == '1':
                print(f"\nLa media es: {media}")
            elif opcion_estadistica == '2':
                print(f"\nLa mediana es: {mediana}")
            elif opcion_estadistica == '3':
                print(f"\nEl cuartil 1 es: {cuartil1}")
            elif opcion_estadistica == '4':
                print(f"\nEl cuartil 3 es: {cuartil3}")
            elif opcion_estadistica == '5':
                if isinstance(frecuencias_moda, dict):
                    if len(frecuencias_moda) > 1:
                        modas = ', '.join(map(str, frecuencias_moda.keys()))
                        frecuencia = list(frecuencias_moda.values())[0]
                        print(f"\nLas modas son {modas}. Su frecuencia es {frecuencia}")
                    else:
                        print(f"\nNo hay moda. La frecuencia de todos los valores es {list(frecuencias_moda.values())[0]}")
                else:
                    print(frecuencias_moda)
            elif opcion_estadistica == '6':
                print(f"\nFrecuencia Absoluta: {frec_abs}")
            elif opcion_estadistica == '7':
                print(f"\nFrecuencia Absoluta Acumulada: {frec_abs_acum}")
            elif opcion_estadistica == '8':
                print(f"\nFrecuencia Relativa: {frec_rel}")
            elif opcion_estadistica == '9':
                print(f"\nFrecuencia Relativa Acumulada: {frec_rel_acum}")
            elif opcion_estadistica == '10':
                print(f"\nFrecuencia Porcentual: {frec_porcentual}")
            elif opcion_estadistica == '11':
                print(f"\nFrecuencia Porcentual Acumulada: {frec_porcentual_acum}")
            elif opcion_estadistica == '12':
                print(f"\nEl Desvío Estándar Muestral es: {desvio_muestral}")
            elif opcion_estadistica == '13':
                print(f"\nEl Desvío Estándar Poblacional es: {desvio_poblacional}")
            elif opcion_estadistica == '14':
                if curtosis < 0:
                    interpretacion = "Platicúrtica"
                elif curtosis == 0:
                    interpretacion = "Mesocúrtica"
                elif curtosis > 0:
                    interpretacion = "Leptocúrtica"    
                
                print(f"\nEl coeficiente de curtosis es: {curtosis:.4f} ({interpretacion})")
            elif opcion_estadistica == '0':
                return  # Salir de la función y volver al menú principal
            else:
                print(f"Opción {opcion_estadistica} no válida. Por favor, intente de nuevo.")  # Mensaje de error si la opción no es válida.

        continuar = input("\n¿Desea realizar otro cálculo de estadística descriptiva? (s/n): ").lower()
        if continuar != 's':
            break

def ejecutar_probabilidad():
    while True:
        mostrar_menu_probabilidad()
        opcion_probabilidad = obtener_opcion_valida("Seleccione una opción: ", [0, 1, 2, 3, 4])

        if opcion_probabilidad == 1:
            while True:
                # Validación para el número de ensayos (n)
                while True:
                    try:
                        n = int(input("\nIngrese el número de ensayos (n): "))
                        if n < 1:
                            print("El número de ensayos (n) debe ser al menos 1.")
                        else:
                            break
                    except ValueError:
                        print("Entrada no válida. Ingrese un número entero para n.")

                # Validación para la probabilidad de éxito (p)
                while True:
                    try:
                        p = float(input("Ingrese la probabilidad de éxito en cada ensayo (p): "))
                        if p < 0 or p > 1:
                            print("La probabilidad (p) debe estar entre 0 y 1.")
                        else:
                            break
                    except ValueError:
                        print("Entrada no válida. Ingrese un número decimal para p.")
                
                mostrar_menu_probabilidad_especifica('binomial')
                opcion_binomial = obtener_opcion_valida("Seleccione una opción: ", [0, 1, 2, 3, 4, 5])
                if opcion_binomial == 0:
                    break

                # Validación para el número de éxitos deseados (k)
                while True:
                    try:
                        k = int(input("Ingrese el número de éxitos deseados (k): "))
                        if k < 1 or k > n:
                            print(f"El número de éxitos (k) debe estar entre 1 y {n}.")
                        else:
                            break
                    except ValueError:
                        print("Entrada no válida. Ingrese un número entero para k.")

                probabilidad_decimal, probabilidad_porcentaje, prob_string = calcular_probabilidades_binomial(n, p, k, opcion_binomial)
                print(f"\n{prob_string} = {probabilidad_decimal} ({probabilidad_porcentaje}%)")

                continuar = input("\n¿Desea realizar otro cálculo con la distribución binomial? (s/n): ").lower()
                if continuar != 's':
                    break

        elif opcion_probabilidad == 2:
            while True:
                # Validación para el número promedio de ocurrencias (λ)
                while True:
                    try:
                        u = float(input("\nIngrese el número promedio de ocurrencias o esperanza (λ): "))
                        if u <= 0:
                            print("El número promedio de ocurrencias (λ) debe ser mayor que 0.")
                        else:
                            break
                    except ValueError:
                        print("Entrada no válida. Ingrese un número decimal positivo para λ.")

                mostrar_menu_probabilidad_especifica('poisson')
                opcion_poisson = obtener_opcion_valida("Seleccione una opción: ", [0, 1, 2, 3, 4, 5])
                if opcion_poisson == 0:
                    break

                # Validación para el número de éxitos deseados (k)
                while True:
                    try:
                        k = int(input("Ingrese el número de éxitos deseados (k): "))
                        if k < 0:
                            print("El número de éxitos deseados (k) debe ser al menos 0.")
                        else:
                            break
                    except ValueError:
                        print("Entrada no válida. Ingrese un número entero para k.")

                probabilidad_decimal, probabilidad_porcentaje, prob_string = calcular_probabilidades_poisson(u, k, opcion_poisson)
                print(f"\n{prob_string} = {probabilidad_decimal} ({probabilidad_porcentaje}%)")

                continuar = input("\n¿Desea realizar otro cálculo con la distribución Poisson? (s/n): ").lower()
                if continuar != 's':
                    break

        elif opcion_probabilidad == 3:
            while True:    
                # Ingresar valores para N, M y n con manejo de errores
                while True:
                    try:
                        N = int(input("\nIngrese el tamaño de la población (N): "))
                        if N >= 1:
                            break
                        else:
                            print("El tamaño de la población (N) debe ser al menos 1. Intente de nuevo.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número entero para N.")

                while True:
                    try:
                        M = int(input("Ingrese cantidad de éxitos en la población (M): "))
                        if 1 <= M <= N:
                            break
                        else:
                            print("La cantidad de éxitos en la población (M) debe ser al menos 1 y no puede ser mayor que N. Intente de nuevo.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número entero para M.")

                while True:
                    try:
                        n = int(input("Ingrese el tamaño de la muestra (n): "))
                        if 1 <= n <= N:
                            break
                        else:
                            print("El tamaño de la muestra (n) debe ser al menos 1 y no puede ser mayor que N. Intente de nuevo.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número entero para n.")
                
                mostrar_menu_probabilidad_especifica('hipergeometrica')
                opcion_hipergeometrica = obtener_opcion_valida("Seleccione una opción: ", [0, 1, 2, 3, 4, 5])
                if opcion_hipergeometrica == 0:
                    break

                # Ingresar valor para k después de seleccionar el tipo de probabilidad
                while True:
                    try:
                        k = int(input("Ingrese cantidad de éxitos buscados en la muestra (k): "))
                        if 0 <= k <= min(M, n):  # k puede ser 0 en la distribución hipergeométrica
                            break
                        else:
                            print(f"La cantidad de éxitos buscados en la muestra (k) debe estar entre 0 y el menor valor entre M y n ({min(M, n)}). Intente de nuevo.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número entero para k.")
                
                probabilidad_decimal, probabilidad_porcentaje, prob_string = calcular_probabilidades_hipergeometrica(M, k, n, N, opcion_hipergeometrica)
                print(f"\n{prob_string} = {probabilidad_decimal} ({probabilidad_porcentaje}%)")

                continuar = input("\n¿Desea realizar otro cálculo con la distribución hipergeométrica? (s/n): ").lower()
                if continuar != 's':
                    break

        elif opcion_probabilidad == 4:
            while True:
                # Ingresar media y desviación estándar con manejo de errores
                while True:
                    try:
                        m = float(input("\nIngrese media: "))
                        break
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número válido para la media.")

                while True:
                    try:
                        s = float(input("Ingrese desviación estándar (σ): "))
                        if s > 0:
                            break
                        else:
                            print("La desviación estándar (σ) debe ser mayor que 0. Intente de nuevo.")
                    except ValueError:
                        print("Entrada inválida. Por favor, ingrese un número válido para la desviación estándar.")

                mostrar_menu_probabilidad_especifica('normal')
                opcion_normal = obtener_opcion_valida("Seleccione una opción: ", [0, 1, 2, 3, 4])
                if opcion_normal == 0:
                    break
                
                if opcion_normal in [1, 2]: # Un valor
                    while True:
                        try:
                            a = float(input("Ingrese el valor de a: "))
                            datos_x = [a]
                            break
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número válido para a.")
                elif opcion_normal in [3, 4]:  # Dos valores
                    while True:
                        try:
                            a = float(input("Ingrese el valor de a: "))
                            break
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número válido para a.")
                    
                    while True:
                        try:
                            b = float(input("Ingrese el valor de b: "))
                            if a != b:
                                # Asegurarse de que 'a' sea menor que 'b'
                                if a < b:
                                    datos_x = [a, b]
                                else:
                                    datos_x = [b, a]
                                break
                            else:
                                print("Los valores de 'a' y 'b' no pueden ser iguales. Intente de nuevo.")
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número válido para b.")

                probabilidad_decimal, probabilidad_porcentaje, prob_string, z_values = calcular_probabilidad_distribucion_normal(m, s, datos_x, opcion_normal)
                z_values_string = ", ".join([f"Z = {z:.4f}" for z in z_values])

                print(f"\nUsando los valores {z_values_string}, {prob_string} = {probabilidad_decimal} ({probabilidad_porcentaje}%)")
                
                continuar = input("\n¿Desea realizar otro cálculo con la distribución normal? (s/n): ").lower()
                if continuar != 's':
                    break

        elif opcion_probabilidad == 0:
            break

        else:
            print(f"Opción {opcion_probabilidad} no válida. Por favor, intente de nuevo.")  # Mensaje de error si la opción no es válida.

# Ciclo principal del programa
def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = obtener_opcion_valida("Seleccione una opción: ", [0, 1, 2])

        if opcion_principal == 1:
            ejecutar_estadistica_descriptiva()
        elif opcion_principal == 2:
            ejecutar_probabilidad()
        elif opcion_principal == 0:
            print("¡Gracias por utilizar el programa!")
            break

if __name__ == "__main__":
    main()