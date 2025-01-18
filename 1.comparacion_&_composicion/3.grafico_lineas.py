'''
El gráfico de líneas es mejor para seguir los cambios a lo largo del tiempo. Para 
percibir cambios pequeños es mejor el gráfico de líneas en vez que el de barras.
'''
import matplotlib.pyplot as plt
import statistics as sta
import pandas as pd 

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

tempe_max = [65, 54, 32, 35, 44, 40, 58]
df = pd.DataFrame(dias, tempe_max)

plt.plot(dias,tempe_max)
plt.title('La temperatura de una semana')
plt.xlabel('Días de la semana')
plt.ylabel('Temperaturas máximas por día')
plt.show()
