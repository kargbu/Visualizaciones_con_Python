'''
Normalmente utilizamos un correlograma
para mostrar los datos de correlación a lo 
largo de un periodo de tiempo.
'''
import numpy as np
import matplotlib.pyplot as plt

# Establecer una semilla para la generación de números aleatorios para reproducibilidad
np.random.seed(2434548631)

# Generar dos conjuntos de 100 números aleatorios siguiendo una distribución normal
x, y = np.random.randn(2, 100)

# Crear una figura y un conjunto de ejes
#fig, ax1 = plt.subplots()
fig, [ax1,ax2]  = plt.subplots(2,1)

# Calcular y mostrar la correlación cruzada entre x e y
ax1.xcorr(x, y, usevlines=True, maxlags=50, normed=True, lw=2)

# Añadir otra figura
ax2.acorr(x, usevlines=True, normed=True, maxlags=50, lw=2)
ax2.grid(True)
plt.show()

# Mostrar el gráfico
plt.show()
