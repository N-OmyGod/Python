import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 25)
y = np.array([(0.5) * i**2 for i in x])
plt.stem(x, y)
plt.show()
