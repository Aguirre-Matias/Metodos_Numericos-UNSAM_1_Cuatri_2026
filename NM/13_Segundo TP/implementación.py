# 2° TP: Interpolación e integración de datos de un ECG
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev
import Funciones as func
import datos_ECG as datos

# Datos del ECG (enunciado del TP)
t = datos.X
y = datos.Y

# Compatibilidad: en NumPy 2 trapz pasó a llamarse trapezoid
trapz = getattr(np, "trapz", np.trapezoid)

# ---------------------------------------------------------------------------
# 1) Graficar la señal completa e identificar ciclos cardíacos
# ---------------------------------------------------------------------------

plt.figure(1)
plt.subplot(2,1,1) # Esto genera una ventana (figure) dividida en 4 y grafica en posicion 1
plt.axis([0,125,-0.2,0.8])
plt.plot(t, y, marker="*", linestyle="", color="red", label="Señal ECG completa")

plt.axvline(x=8, color='purple', linestyle='--')
plt.axvline(x=95, color='purple', linestyle='--', label='Ciclo cardíaco completo')
plt.annotate('Ciclo cardíaco completo', xy=(70, 0.4), xytext=(70, 0.4), fontsize=10, fontname='arial', color='purple', bbox=dict(facecolor='yellow', alpha=0.3)) # Color de fondo del cuadro

plt.xlabel("t (s)")
plt.ylabel("Amplitud")
plt.title("ciclo cardíaco completo")
plt.grid(True)
plt.legend()

plt.subplot(2,1,2) # Esto genera una ventana (figure) dividida en 4 y grafica en posicion 1
plt.axis([0,125,-0.2,0.8])
plt.plot(t, y, marker="*", linestyle="--", color="blue", label="Señal ECG completa")

plt.axvline(x=24, color='green', linestyle='--')
plt.axvline(x=111, color='green', linestyle='--', label='Intervalo R-R')
plt.annotate('Intervalo R-R', xy=(111, 0.5), xytext=(115, 0.5), fontsize=10, fontname='arial', color='green', bbox=dict(facecolor='yellow', alpha=0.3)) # Color de fondo del cuadro

plt.axvline(x=14, color='gray', linestyle='--')
plt.axvline(x=21, color='gray', linestyle='--', label='Segmento P-R')
plt.annotate('Segmento P-R', xy=(0, 0), xytext=(29, 0.15), fontsize=10, fontname='arial', color='gray', bbox=dict(facecolor='yellow', alpha=0.3)) # Color de fondo del cuadro

plt.axvline(x=21, color='orange', linestyle='--')
plt.axvline(x=40, color='orange', linestyle='--', label='Complejo QRS')
plt.annotate('Complejo QRS', xy=(40, 0.5), xytext=(27, 0.5), fontsize=10, fontname='arial', color='orange', bbox=dict(facecolor='yellow', alpha=0.3)) # Color de fondo del cuadro

plt.axvline(x=21, color='purple', linestyle='--')
plt.axvline(x=78, color='purple', linestyle='--', label='Intervalo Q-T')
plt.annotate('Intervalo Q-T', xy=(78, 0.5), xytext=(82, 0.5), fontsize=10, fontname='arial', color='purple', bbox=dict(facecolor='yellow', alpha=0.3)) # Color de fondo del cuadro

plt.xlabel("t (s)")
plt.ylabel("Amplitud")
plt.title("Señal ECG completa R-R (unidos por --) ")
plt.grid(True)
plt.legend()

# ---------------------------------------------------------------------------
# 3 y 4) Gráfico del ciclo aislado con asteriscos rojos, polinomio interpolador y polinomio interpolador por spline
# ---------------------------------------------------------------------------
# Solo los puntos del ciclo elegido
inicio_ciclo = 8
fin_ciclo = 96
t_ciclo = t[inicio_ciclo:fin_ciclo]    
y_ciclo = y[inicio_ciclo:fin_ciclo]
grado = len(t_ciclo) - 1   

# No pude lograr que el pol interpolar con poly fit quede igual a los datos
cof = np.polyfit(t_ciclo, y_ciclo, grado)
rf = np.arange(t_ciclo[0], t_ciclo[-1] + 0.01, 0.01)
y_poly = np.polyval(cof, rf)

spl= splrep(t_ciclo, y_ciclo, k=3)
y_spline = splev(rf,spl)

plt.subplot(2,1,1) # Esto genera una ventana (figure) dividida en 4 y grafica en posicion 1
plt.plot(rf,y_spline,label = "Polinomio interpolador (spline)", marker="", linestyle="-", color="blue")
plt.plot(rf,y_poly,label = "Polinomio interpolador (polyfit)", marker="", linestyle="-", color="green")
plt.legend()

plt.show()

# ---------------------------------------------------------------------------
# 5) Integración del ciclo completo
# ---------------------------------------------------------------------------
# 5.1 Integración analítica del polinomio interpolador (polyint / polyval)
cof_int = np.polyint(cof)
I_poly = np.polyval(cof_int, t[fin_ciclo]) - np.polyval(cof_int, t[inicio_ciclo])

# 5.2 Método de trapecios (trapz) sobre los datos discretos del ciclo
I_trapz = trapz(y_ciclo, t_ciclo)

# 5.3 Simpson compuesto (código de clase) sobre la función polinomial
f_poly = lambda x: np.polyval(cof, x)
h = 0.1
I_simpson = func.simpCompuestos(f_poly, inicio_ciclo, fin_ciclo, h)

print("\n integral del ciclo completo [",inicio_ciclo, ";", fin_ciclo, "] s:")
print("  5.1 Polinomio (polyint):", I_poly)
print("  5.2 Trapecios (trapz):  ", I_trapz)
print("  5.3 Simpson compuesto:  ", I_simpson, "  (h =", h, ")")

# Diagnóstico (normal entre 0.20 y 0.50)
I_ref = I_trapz
if 0.20 <= I_ref <= 0.50:
    print("\nDiagnóstico: ECG NORMAL (Integral =", round(I_ref, 4), ")")
else:
    print("\nDiagnóstico: ECG PATOLÓGICO (Integral =", round(I_ref, 4), ")")

# */