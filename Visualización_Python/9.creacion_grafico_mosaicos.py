'''
Los gráficos de mosaico le permiten examinar la relación entre dos o más variables categóricas. 
Por ejemplo, país y género.
'''
from statsmodels.graphics.mosaicplot import mosaic
import pandas as pd
import matplotlib.pyplot as plt

# Crear el DataFrame con las etiquetas en español
myDataframe = pd.DataFrame({
    'País': ['US', 'Canada', 'US', 'México', 'US', 'Canada'],
    'Género': ['H', 'M', 'H', 'M', 'M', 'M']
})
print(myDataframe)

# Generar el gráfico de mosaico
mosaic(myDataframe, ['País', 'Género'])

# Mostrar el gráfico
plt.show()
