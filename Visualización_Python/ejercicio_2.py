import matplotlib.pyplot as plt

data = [17, 72, 45, 86, 96, 24, 27, 32, 38, 94, 70]

plt.boxplot(data)
plt.title('Gráfica de caja con datos aleatorios')
plt.xlabel('Conjuntos de datos')
plt.ylabel('Valores')
plt.show()