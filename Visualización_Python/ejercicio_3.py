import numpy as np
import matplotlib.pyplot as plt

sectores = ['Energía', 'Salud', 'Tecnología', 'Productos de primera necesidad']
regiones = ['Norte América', 'Europa', 'Asia', 'Latino América']
performance = np.array([
    [12, -8, 15, 4],
    [7, 10, 5, -3],
    [20, 3, 18, 8],
    [1, -5, 2, 0]
])

# Crear una figura y un eje
fig, ax = plt.subplots()

# Mostrar los retornos como una imagen (matriz de calor)
im = ax.imshow(performance, cmap="coolwarm")

# Queremos mostrar todas las marcas...
ax.set_xticks(np.arange(len(regiones)))
ax.set_yticks(np.arange(len(sectores)))

# ...y etiquetarlas con las entradas de las respectivas listas
ax.set_xticklabels(regiones)
ax.set_yticklabels(sectores)

# Establecer el título del gráfico
ax.set_title("Rendimiento del sector por región")

# Añadir una barra de color
cbar = ax.figure.colorbar(im, ax=ax)
cbar.ax.set_ylabel("Cambio de rendimiento (%)", rotation=-90, va="bottom")

# Ajustar el diseño para que los elementos no se solapen
fig.tight_layout()

# Mostrar el gráfico
plt.show()
