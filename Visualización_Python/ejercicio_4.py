'''
Importe las bibliotecas necesarias y establezca una semilla aleatoria para la reproducibilidad.
Genere dos conjuntos aleatorios de datos, x y y,cada uno con 100 puntos.
Cree un subdiagrama y utilice la función xcorr para trazar el correlograma.
Asegúrese de utilizar líneas verticales (usevlines=True), establezca el número máximo de 
retardos en 50 (maxlags=50), normalice los datos (normed=True) y establezca el ancho de línea en 2 (lw=2).
'''
# WRITE YOUR CODE HERE
import numpy as np
import matplotlib.pyplot as plt

# Establecer una semilla para la generación de números aleatorios para reproducibilidad
np.random.seed(31416)

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
