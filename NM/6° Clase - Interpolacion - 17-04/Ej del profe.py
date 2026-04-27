# Para limpiar la terminal antes de continuar
# Desde acá

#import os

#os.system('cls' if os.name == 'nt' else 'clear')

import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,10,0.1)
# print("t = ",t)

f= lambda x: np.sin(x)
g= np.cos(t)

print("f(1) = ", f(1))

# PLOT

plt.figure(1) # Crear una ventana donde graficar
plt.plot(t,f(t), label = "Funcion Seno", marker=".", linestyle=":", color="red") # Grafico t y f(t) y le pongo atributos
# Identificar los puntos, la forma de lina, el color
plt.plot(t,g, label = "Funcion Coseno", marker="x", linestyle="-", color="blue")
plt.xlabel("t") # Nombre del eje X
plt.ylabel("f(t)") # Nombre del eje Y
plt.title("Funciones Trigonometricas") # Titulo del grafico
plt.grid() # Grilla del grafico
plt.legend() # Leyenda de los graficos
plt.axis([0,4,0,1]) # A axis le paso un vector adentro de la funcion --> axis([Xinf, Xsup, Yinf, Ysup])


#plt.show() # Muestra todo lo que se pide para graficar

# Tipos de "linestyle"

# '-': Línea sólida (por defecto).
# '--': Línea discontinua.
# ':': Línea punteada.
# '-.': Línea discontinua-punteada.

# Tipos de "marker"
# '.': Punto pequeño.
# 'o': Círculo.
# 's': Cuadrado.
# 'D': Diamante.
# '^': Triángulo hacia arriba.
# 'v': Triángulo hacia abajo.
# '*': Estrella.
# '+': Cruz.
# 'x': Equis.
# 'None': Sin marcador (por defecto si no se especifica).

# Tipos de "color"

# 'red' (rojo)
# 'blue' (azul)
# 'green' (verde)
# 'yellow' (amarillo)
# 'orange' (naranja)
# 'purple' (morado)
# 'pink' (rosa)
# 'brown' (marrón)
# 'gray' o 'grey' (gris)
# 'black' (negro)
# 'white' (blanco)
# 'cyan' (cian)
# 'magenta' (magenta)

# SUBPLOT
x=np.arange(0,10,0.1)
y1= np.sin(x)
y2= np.cos(x)
y3= np.tan(x)
y4= np.exp(x)

plt.figure(2) # Crear una ventana donde graficar

# Funcion Sin vs Cos
plt.subplot(2,2,1) # Esto genera una ventana (figure) dividida en 4 y grafica en posicion 1
plt.plot(x,y1, marker=".", linestyle="-", color="red") # Grafico t y f(t) y le pongo atributos
plt.xlabel("X") # Nombre del eje X
plt.ylabel("f(X)") # Nombre del eje Y
plt.title("Funciones Seno") # Titulo del grafico
plt.grid() # Grilla del grafico

# Funcion Cos
plt.subplot(2,2,2)
plt.plot(x,y2, marker="x", linestyle="-", color="blue")
plt.xlabel("X") # Nombre del eje X
plt.ylabel("f(X)") # Nombre del eje Y
plt.title("Funciones Cos") # Titulo del grafico
plt.grid() # Grilla del grafico

# Funcion Tan
plt.subplot(2,2,3)
plt.plot(x,y3, marker="*", linestyle="-", color="magenta")
plt.xlabel("X") # Nombre del eje X
plt.ylabel("f(X)") # Nombre del eje Y
plt.title("Funciones Tan") # Titulo del grafico
plt.grid() # Grilla del grafico

# Funcion Exp
plt.subplot(2,2,4)
plt.plot(x,y4, marker="o", linestyle="-", color="black")
plt.xlabel("X") # Nombre del eje X
plt.ylabel("f(X)") # Nombre del eje Y
plt.title("Funciones Exp") # Titulo del grafico
plt.grid() # Grilla del grafico


plt.show()