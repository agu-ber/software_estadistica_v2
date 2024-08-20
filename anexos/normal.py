def formula(M,S,x):
    distribucion_normal = (x - M) / S
    return round(distribucion_normal,2)

"""
M = Media
S = Variacion estandar
"""
M = float(input("Ingrese media: "))
S = float(input("Ingrese variación estandar (Sigma): "))
x = int(input("Ingrese variable aleatoria (x): "))

z = formula(M,S,x)

