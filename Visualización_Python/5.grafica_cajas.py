import matplotlib.pyplot as plt
import statistics as sta
import pandas as pd 
import numpy as np

# La estructura básica plt.boxplot(data)
data=[2,12,23,42,56,75,79,84]
plt.boxplot(data)
plt.title('title name')
plt.xlabel('xAxis name')
plt.ylabel('yAxis name')
plt.show()
