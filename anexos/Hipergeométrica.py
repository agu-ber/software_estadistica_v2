def factorial(x):
    resultado = 1
    for i in range(2, x + 1):
        resultado = resultado * i
    return resultado

def coeficiente_binomial(M,k):
    return factorial(M) / (factorial(k) * factorial(M-k))

def formula(M,k,n,N):
    coeficiente1 = coeficiente_binomial(M,k) 
    coeficiente2 = coeficiente_binomial(N-M,n-k)
    coeficiente3 = coeficiente_binomial(N,n)
    distribucion_hipergeometrico = (coeficiente1 * coeficiente2) / coeficiente3
    return round(distribucion_hipergeometrico, 4)

N = int(input("Ingrese número total de la muestra (N): "))
M = int(input("Ingrese cantidad de éxitos (M): "))
n = int(input("Ingrese elementos del subconjunto (n): "))
k = int(input("Ingrese dato correspondiente (éxitos buscados) (K): "))

probabilidad = formula(M,k,n,N)

print("La probabilidad es de: ", probabilidad )
