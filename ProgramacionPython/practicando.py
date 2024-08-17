#Aprendiendo a utilizar matplotlib
"""
Ejemplos de uso de matplotlib para graficar
"""
#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

# Graficar una función lineal La mas sencilla
values = np.array([1, 2, 3, 4, 5,6,7,8,9,10])
plt.plot(values)
plt.show()