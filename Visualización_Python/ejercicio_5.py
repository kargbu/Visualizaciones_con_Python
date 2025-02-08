import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
data = pd.read_csv('/Users/kgb/Desktop/COURSERA/Visualización_Python/Visualización_Python/moka_data.csv')


# Display DataFrame information
data.info()

# Show the first 5 rows
display(data.head())

# Contar las infecciones por estado
zombi_por_estados = data['States'].value_counts()

# Ajustar el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Crear el gráfico de columnas
zombi_por_estados.plot(kind='bar', color='skyblue')
plt.title('Infección zombi por estado')
plt.xlabel('Estado')
plt.ylabel('Número de infecciones')
plt.xticks(rotation=45)
plt.show()


# Contar las infecciones por género
zombie_by_gender = data['gender'].value_counts()

# Crear el gráfico circular
plt.figure(figsize=(8, 8))
zombie_by_gender.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['lightcoral', 'lightskyblue'])
plt.title('Infección zombi por género')
plt.ylabel('')  # Eliminar la etiqueta del eje y
plt.show()

# Contar las infecciones por género e infección
infected_vs_non_infected = data.groupby(['gender', 'ZOMBIE']).size().unstack()

# Crear el gráfico de columnas apiladas
infected_vs_non_infected.plot(kind='bar', stacked=True, figsize=(10, 6), color=['lightcoral', 'lightskyblue'])
plt.title('Infectados vs No infectados por género')
plt.xlabel('Género')
plt.ylabel('Número de personas')
plt.legend(title='Estado de infección')
plt.show()

