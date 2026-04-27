# # ejercicioooooooooooooooooooooooooooooooooooooooooooooooooooooo
import numpy as np

# pruebas 
import math as mt
# S=0
# k=0

# # contemplar que cuando usamos np.arange este genera un vector de 1 a 4 sin tomar el 5 
# for n in np.arange(1,5,1):
#     S= S + 1/n**2
#     k= k + 1
# print(S)
# print(k)

# Ejercicio 5

def raiz(x,n):
    for i in np.arange(0,n,1):
        x= (1/2)*(x+(2/x))
    return x
    
r = raiz(1/2,10)    
print(r)
print(mt.sqrt(2))
print(np.sqrt(2))

print(mt.pi)
print(np.pi)