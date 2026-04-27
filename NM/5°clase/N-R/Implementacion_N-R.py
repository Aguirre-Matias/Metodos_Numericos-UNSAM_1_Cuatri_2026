import numpy as np
import NewtonRapson as NR

funcion= lambda x:(x**3)-8
# Raiz:2
Dfuncion= lambda y:3*(y**2)

# funcion= lambda x:np.exp(-x)-x
# Dfuncion= lambda y:(-np.exp(-y))-1

tolerancia=float(input("Ingrese la tolerancia deseada: "))
inicio=float(input("Ingrese el punto X0: "))
print("La raiz de F(x) es:",NR.MetNR(inicio,funcion,Dfuncion,tolerancia))