'''
El siguiente gráfico se realiza con Spyder con una orientación diferente al gráfico de
columnas. El gráfico de barras tienen barras horizontales.Básicamente se tiene el mismo
script: 
plt.barh(xAxis,yAxis)
plt.title('title name')
plt.xlabel('xAxis name')
plt.ylabel('yAxis name')
plt.show()
'''
import matplotlib.pyplot as plt
import statistics as sta
import pandas as pd 

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

tempe_max = [65, 54, 32, 35, 44, 40, 58]
df = pd.DataFrame(dias, tempe_max)

print(df)
Colors = ['red','blue','green','brown','purple']
plt.barh(dias,tempe_max,color=Colors)
plt.title('La temperatura de una semana')
plt.xlabel('Temperatura máxima')
plt.ylabel('Días')
plt.show()



