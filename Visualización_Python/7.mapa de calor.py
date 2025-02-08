'''
La sintaxis básica para realizar un mapa de calor es plt.imshow(data).
Un lugar para tener una documentación es el siguiente: 
https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html
'''
import matplotlib.pyplot as plt
import statistics as sta
import pandas as pd 
import numpy as np

import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

# Definir las listas de sectores y geografías
sector = ["Tecnología", "Consumidor discrecional", "Estado real", "Servicios financieros"]
geography = ["Asia", "Europa", "US", "India"]

# Simular retornos del mercado basados en datos aleatorios
returns = np.array([
    [40, 13, 20, 37],
    [30, 41, 37, 46],
    [89, 50, 65, 55],
    [35, 20, 25, 35]
])

# Crear una figura y un eje
fig, ax = plt.subplots()

# Mostrar los retornos como una imagen (matriz de calor)
im = ax.imshow(returns)

# Queremos mostrar todas las marcas...
ax.set_xticks(np.arange(len(sector)))
ax.set_yticks(np.arange(len(geography)))

# ...y etiquetarlas con las entradas de las respectivas listas
ax.set_xticklabels(sector)
ax.set_yticklabels(geography)


# Etiquetar los ejes
ax.set_xlabel("Regiones")
ax.set_ylabel("Sectores")

# Establecer el título del gráfico
ax.set_title("Ingresos por país y por sector en milles de")

# Ajustar el diseño para que los elementos no se solapen
fig.tight_layout()

# Mostrar el gráfico
plt.show()
