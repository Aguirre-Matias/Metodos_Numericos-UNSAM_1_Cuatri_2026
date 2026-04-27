import numpy as np
import  matplotlib.pyplot as plt

t= np.arange(0,10,0.1)
print("t=",t)

f= lambda t: np.sin(t)
g= np.cos(t)

print("f=",f(1))

# PLOT

plt.figure(1) # Crear una ventana donde graficar
plt.plot(t, f(t), label = "Funcion Seno", marker=".", linestyle=":", color="red") # Grafico t y f(t) y le pongo atributos
# Identificar los puntos, la forma de lina, el color
plt.plot(t, g, label = "Funcion Coseno", marker=".", linestyle=":", color="blue")
plt.xlabel("t") # Nombre del eje X
plt.ylabel("f(t)") # Nombre del eje Y
plt.title("Funciones Trigonometricas") # Titulo del grafico
plt.grid() # Grilla del grafico
plt.legend() # Leyenda de los graficos
# plt.pause(0.5) # Pausa de 0.1 segundos
# plt.show() # Muestra todo lo que se pide para graficar
plt.axis([0, 4, 0, 1]) # Limites del grafico a axis le tengo que pasar un vector de 4 elementos [xmin, xmax, ymin, ymax]
# Tipos de "linestyle"

# '-': Línea sólida (por defecto).
# '--': Línea discontinua.
# ':': Línea punteada.
# '-.': Línea discontinua-punteada.
# '': Línea sin estilo.
# 'o': Puntos.
# 's': Cuadrados.
# 'x': Cruces.
# '+': Más.
# 'd': Diamantes.
# 'v': Triángulos hacia abajo.
# '^': Triángulos hacia arriba.
# '<': Triángulos hacia la izquierda.
# '>': Triángulos hacia la derecha.
# 'p': Pentágonos.

# SUBPLOT

x= np.arange(0,10,0.1)
y1= np.sin(x)
y2= np.cos(x)
y3= np.tan(x)
y4= np.exp(x)

plt.figure(2)
# Funcion Seno y coseno 
plt.subplot(2,2,1)
plt.plot(x, y1, marker=".", linestyle=":", color="red")
plt.plot(x, y2, marker=".", linestyle=":", color="green") 
plt.xlabel("t") # Nombre del eje X
plt.ylabel("f(t)") # Nombre del eje Y
plt.title("Funciones seno y coseno") # Titulo del grafico
plt.grid() # Grilla del grafico

# Funcion Coseno
plt.subplot(2,2,2)
plt.plot(x, y2, marker=".", linestyle=":", color="green") 
plt.xlabel("t") # Nombre del eje X
plt.ylabel("f(t)") # Nombre del eje Y
plt.title("Funciones coseno") # Titulo del grafico
plt.grid() # Grilla del grafico

# Funcion tangente
plt.subplot(2,2,3)
plt.plot(x, y3, marker=".", linestyle=":", color="blue") 
plt.xlabel("t") # Nombre del eje X
plt.ylabel("f(t)") # Nombre del eje Y
plt.title("Funciones tangente") # Titulo del grafico
plt.grid() # Grilla del grafico

# Funcion exponencial
plt.subplot(2,2,4)
plt.plot(x, y4,marker=".", linestyle=":", color="yellow") 
plt.xlabel("t") # Nombre del eje X
plt.ylabel("f(t)") # Nombre del eje Y
plt.title("Funciones exponencial") # Titulo del grafico
plt.grid() # Grilla del grafico
# plt.legend() # Leyenda de los graficos
plt.show()

