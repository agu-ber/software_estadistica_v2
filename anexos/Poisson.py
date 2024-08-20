def factorial(x):
    resultado = 1
    for i in range(2, x + 1):
        resultado = resultado * i
    return resultado

def formula(x,u):
    e = 2.7183
    distribucion_poisson = ((e ** -u) * (u**x)) / factorial(x)
    return round(distribucion_poisson,4)

x = int(input("Ingrese variable aleatoria (x): "))
u = int(input("Ingrese valor de lambda (λ): "))

probabilidad = formula(x,u)

print("La probabilidad es de: ", probabilidad )

