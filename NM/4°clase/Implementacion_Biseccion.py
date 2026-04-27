# implementacion del metodo de biseccion.
import numpy as np
import ecnolineales as ECNL

# funcion= lambda x:(x**2)-1
funcion= lambda x:np.exp(-x)-x
a=float(input("primer intervalo: "))
b=float(input("segundo intervalo: "))
n=int(input("cantidad de iteraciones: "))

r= ECNL.Bisec(a,b,funcion,n)
print(r) 

