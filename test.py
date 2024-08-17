import matplotlib as plt
import numpy as np
##Generando una grafica sencilla

values = np.random.randint(low=1, high=30, size=10)
plt.plot(values)
plt.show()