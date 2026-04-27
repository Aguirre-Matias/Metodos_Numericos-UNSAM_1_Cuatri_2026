import numpy as np
import  matplotlib.pyplot as plt

t= np.arange(0,10,0.1)

f= lambda t: np.sin(t)
g= np.cos(t)

# PLOT
plt.figure(1) # Crear una ventana donde graficar
plt.grid() # Grilla del grafico
plt.legend() # Leyenda de los graficos
plt.axis([0, 10, -1.5, 1.5]) # Limites del grafico a axis le tengo que pasar un vector de 4 elementos [xmin, xmax, ymin, ymax]

for i in np.arange(0,10,0.1):
    plt.plot(i, f(i), label = "Funcion Seno", marker=".", linestyle=":", color="red") # Grafico t y f(t) y le pongo atributos
    # Identifcar los puntos, la forma de lina, el color
    # plt.plot(i, g, label = "Funcion Coseno", marker=".", linestyle=":", color="blue")
    plt.xlabel("t") # Nombre del eje X
    plt.ylabel("f(t)") # Nombre del eje Y
    plt.title("Funciones Trigonometricas") # Titulo del grafico
    plt.pause(0.1) # Pausa de 0.1 segundos
plt.show() # Muestra todo lo que se pide para graficar
