import matplotlib.pyplot as plt
import statistics as sta
import pandas as pd

# Esta es la sintaxis básica plt.scatter(x, y)

import random
x = random.sample(range(100),20)
y = random.sample(range(100),20)
print(x)
print(y)

x = [66, 72, 5, 91, 46, 70, 65, 96, 68, 17, 51, 83, 13, 8, 45, 63, 21, 11, 97, 54]
y = [72, 54, 55, 2, 29, 41, 90, 30, 7, 33, 47, 39, 63, 58, 73, 85, 66, 11, 14, 4]
plt.scatter(x, y)
plt.show()