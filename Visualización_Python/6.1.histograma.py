import matplotlib.pyplot as plt
import statistics as sta
import pandas as pd 
import numpy as np

altura = np.random.normal(170, 10, 250)

plt.hist(altura)
plt.title('frecuencia de números.')
plt.xlabel('altura')
plt.ylabel('frecuencia')
plt.show()