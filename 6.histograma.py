import matplotlib.pyplot as plt
import statistics as sta
import pandas as pd 
import numpy as np

height = np.random.normal(170, 10, 250)

plt.hist(height)
plt.title('height frequency ')
plt.xlabel('height')
plt.ylabel('frequency')
plt.show()