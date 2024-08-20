import statistics  # Importa el módulo statistics para realizar cálculos estadísticos.

def convertir_datos(datos):
    datos_lista = datos.split(",")  # Divide la cadena en una lista donde cada elemento se separa por una coma.
    datos_convertidos = []  # Define una lista vacía donde se guardarán los datos.
    for dato in datos_lista:  # Itera sobre cada dato en la lista de datos.
        if "." in dato:  # Si el dato contiene un punto, se considera decimal.
            datos_convertidos.append(float(dato))  # Convierte a float y lo agrega a la lista.
        else:
            datos_convertidos.append(int(dato))  # Si no, convierte a entero y lo agrega a la lista.
    return datos_convertidos  # Retorna la lista de datos convertidos.

def calcular_estadisticas(datos):
    n = len(datos)  # Calcula la cantidad de datos.
    media = round(sum(datos) / n, 4)  # Calcula la media con 4 decimales.
    mediana = round(statistics.median(datos), 4)  # Calcula la mediana con 4 decimales.
    datos_inferiores = [n for n in datos if n < mediana]  # Filtra los datos inferiores a la mediana.
    datos_superiores = [n for n in datos if n > mediana]  # Filtra los datos superiores a la mediana.
    cuartil1 = round(statistics.median(datos_inferiores), 4)  # Calcula el primer cuartil con 4 decimales.
    cuartil3 = round(statistics.median(datos_superiores), 4)  # Calcula el tercer cuartil con 4 decimales.
    moda = statistics.multimode(datos)  # Calcula la moda.
    varianza_muestral = sum((xi - media) ** 2 for xi in datos) / (n - 1)  # Calcula la varianza muestral.
    varianza_poblacional = sum((xi - media) ** 2 for xi in datos) / n  # Calcula la varianza poblacional.
    desvio_muestral = round(varianza_muestral ** 0.5, 4)  # Calcula el desvío estándar muestral con 4 decimales.
    desvio_poblacional = round(varianza_poblacional ** 0.5, 4)  # Calcula el desvío estándar poblacional con 4 decimales.
    return media, mediana, cuartil1, cuartil3, moda, desvio_muestral, desvio_poblacional  # Retorna cada cálculo previo.

def calcular_frecuencias(datos):
    n = len(datos)
    datos.sort()  # Ordena los datos.

    frec_abs = {}  # Frecuencia Absoluta.
    for dato in datos:
        if dato in frec_abs:
            frec_abs[dato] += 1
        else:
            frec_abs[dato] = 1

    frec_rel = {k: round(v / n, 4) for k, v in frec_abs.items()}  # Frecuencia Relativa.
    frec_porcentual = {k: round(v * 100, 2) for k, v in frec_rel.items()}  # Frecuencia Porcentual.

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

    frec_porcentual_acum = {k: round(v * 100, 2) for k, v in frec_rel_acum.items()}  # Frecuencia Porcentual Acumulada.
    
    return frec_abs, frec_rel, frec_porcentual, frec_abs_acum, frec_rel_acum, frec_porcentual_acum

def mostrar_menu_estadistica_descriptiva():
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
    print("0. Volver al Menú Principal\n")

def mostrar_menu_probabilidad():
    print("\nMenú de Probabilidad:")
    print("1. Distribución Binomial")
    print("2. Distribución Poisson")
    print("3. Distribución Hipergeométrica")
    print("4. Distribución Normal")
    print("5. Coeficiente de Curtosis")
    print("0. Volver al Menú Principal\n")

def obtener_datos():
    datos_entrada = input("Ingrese los datos separados por comas: ")
    return convertir_datos(datos_entrada)

def main():
    while True:
        print("Seleccione el módulo que desea utilizar:")
        print("1. Estadística Descriptiva")
        print("2. Probabilidad")
        print("0. Salir\n")
        eleccion = input("Ingrese su elección: ")

        if eleccion == "1":
            datos_entrada = input("\nIngrese los datos separados por comas: ")
            datos = convertir_datos(datos_entrada)
            media, mediana, cuartil1, cuartil3, moda, desvio_muestral, desvio_poblacional = calcular_estadisticas(datos)
            frec_abs, frec_rel, frec_porcentual, frec_abs_acum, frec_rel_acum, frec_porcentual_acum = calcular_frecuencias(datos)
            
            while True:
                mostrar_menu_estadistica_descriptiva()
                opciones = input("Ingrese los números de las opciones que desea, separados por comas: ").split(',')
                if "0" in opciones:
                    break
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
                        print("\nFrecuencia Porcentual: ")
                        for k, v in frec_porcentual.items():
                            print(f"{k}: {v}%")
                    elif opcion == "11":
                        print("\nFrecuencia Porcentual Acumulada: ")
                        for k, v in frec_porcentual_acum.items():
                            print(f"{k}: {v}%")
                    elif opcion == "12":
                        print(f"\nDesvío Estándar Muestral: {desvio_muestral}")
                    elif opcion == "13":
                        print(f"\nDesvío Estándar Poblacional: {desvio_poblacional}")
                    else:
                        print(f"\nOpción {opcion} no válida. Por favor, intente de nuevo.")
                
                otra_opcion = input("\n¿Desea calcular otra cosa? (s/n): ")
                if otra_opcion.lower() != "s":
                    break

        elif eleccion == "2":
            while True:
                mostrar_menu_probabilidad()
                opcion_probabilidad = input("Ingrese el número de la opción que desea: ")
                if opcion_probabilidad == "0":
                    break
                elif opcion_probabilidad in ["1", "2", "3", "4", "5"]:
                    print(f"\nOpción {opcion_probabilidad} seleccionada. (Funcionalidad en desarrollo)")
                else:
                    print("\nOpción no válida. Intente de nuevo.")
                
                otra_opcion = input("\n¿Desea calcular otra cosa? (s/n): ")
                if otra_opcion.lower() != "s":
                    break

        elif eleccion == "0":
            print("\nGracias por usar el programa.")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()
