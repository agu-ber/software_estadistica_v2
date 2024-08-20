def factorial(x):
    resultado = 1
    for i in range(2, x + 1):
        resultado = resultado * i
    return resultado

def coeficiente_binomial(n,k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def formula(n, k, p ):
    coeficiente = coeficiente_binomial(n,k)
    distribucion_binomial = coeficiente * (p ** k) * ((1 - p) ** (n-k))
    return round(distribucion_binomial, 4)

n = int(input("Ingrese número de ensayos (n): "))
p = float(input("Ingrese probabilidad de éxito (p): "))
k = int(input("Ingrese número de éxitos deseados (k): "))

probabilidad = formula(n,k,p)

print("La probabilidad de obtener exactamente ", k , "éxitos en", n, "ensayos es: ", probabilidad )