# Usaremos Spyder
import pandas as pd
import matplotlib.pyplot as plt

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

tempe_max = [65, 54, 32, 35, 44, 40, 58]
df = pd.DataFrame(dias, tempe_max)

Colores = ['red', 'blue','green','brown','purple']
plt.bar(dias, tempe_max, color=Colores)
plt.title('Gráfica de barras')
plt.xlabel('Días')
plt.ylabel('Temperatura máxima')
plt.show()
