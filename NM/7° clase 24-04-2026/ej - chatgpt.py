import matplotlib.pyplot as plt
import numpy as np

# 1. Crear datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 2. Encontrar las coordenadas del punto máximo
x_max = x[np.argmax(y)]
y_max = y.max()

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Señal')

# 3. Agregar la etiqueta con una flecha (annotate)
plt.annotate(f'Máximo: {y_max:.2f}', 
             xy=(x_max, y_max),       # Dónde apunta la flecha
             xytext=(x_max + 1, y_max), # Dónde se sitúa el texto
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12,
             color='red')

# Opcional: un punto rojo para que destaque más
plt.scatter(x_max, y_max, color='red')

plt.title("Gráfico con Etiqueta de Punto Máximo")
plt.legend()
plt.show()