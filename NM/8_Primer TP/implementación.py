# implementacion del metodo de biseccion.
import numpy as np
import Funciones as func
import matplotlib.pyplot as plt
import sys

# funcion a resolver:
funcion= lambda x: x+(3/2)*np.exp(-np.sin(2*x))
Dfuncion= lambda y: 1-3*np.exp(-np.sin(2*y))*np.cos(2*y) # derivada de la funcion

a=-2
b=10
n=5
error=0.0005 #Error ABSOLUTO

print("Se inicia el programa utilizando el intervalo: [",a,";",b,"], con",n,"iteraciones para el metodo de biseccion y un error absoluto pretendido de",error,"para el metodo de Newton Rapshon")

# Metodo de Biseccion y Newton Rapshon
raiz, inter_a, inter_b, iteraciones= func.B_NR(funcion,Dfuncion,n,a,b,error)

if raiz is None:
    print("- SE CIERRA EL PROGRAMA -")
    sys.exit(1)

print("- El intervalo alcanzado por el metodo de biseccion fue [", inter_a, ";", inter_b,"]")
print("- La cantidad de iteraciones realizadas en el Método de Newton Rapshon fueron:", iteraciones)
print("- La raiz encontrada fue:", raiz)

print("-----------------------------------------------------------------------------")
print("Se proponen los intervalos de arranque [-3,9;-2] y [-5;-3,9] para obtener otra solucion de la ecuacion")
print("Para el intervalo [-3,9;-2] se obtiene:")
raiz2, inter_a2, inter_b2, iteraciones2= func.B_NR(funcion,Dfuncion,n,-3.9,-2,error)
print("- El intervalo alcanzado por el metodo de biseccion fue [", inter_a2, ";", inter_b2,"]")
print("- La cantidad de iteraciones realizadas en el Método de Newton Rapshon fueron:", iteraciones2)
print("- La raiz encontrada fue:", raiz2)

print("Para el intervalo [-5;-3,9] se obtiene:")
raiz3, inter_a3, inter_b3, iteraciones3= func.B_NR(funcion,Dfuncion,n,-5,-3.9,error)
print("- El intervalo alcanzado por el metodo de biseccion fue [", inter_a3, ";", inter_b3,"]")
print("- La cantidad de iteraciones realizadas en el Método de Newton Rapshon fueron:", iteraciones3)
print("- La raiz encontrada fue:", raiz3)

t= np.arange(-5,10.1,0.1)
plt.figure(1)
plt.plot(t, funcion(t), label = "Funcion evaluada", marker="", linestyle="-", color="blue")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funcion evaluada por el metodo de biseccion y Newton Rapshon")
plt.grid()
plt.legend()
plt.axis([-5, 10, -4, 14])

plt.show()

a2=float(input("Proponga otro punto de inicio: "))
b2=float(input("Proponga otro punto de fin: "))

raiz4, inter_a4, inter_b4, iteraciones4= func.B_NR(funcion,Dfuncion,n,a2,b2,error)
if raiz4 is None:
    print("- SE CIERRA EL PROGRAMA -")
    sys.exit(1)
print("- El intervalo alcanzado por el metodo de biseccion fue [", inter_a4, ";", inter_b4,"]")
print("- La cantidad de iteraciones realizadas en el Método de Newton Rapshon fueron:", iteraciones4)
print("- La raiz encontrada fue:", raiz4)