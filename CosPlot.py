import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 200)   # start,stop,step
y = np.cos(x)
z = np.cos(0.5*x)

plt.plot(x, np.cos(x), x, np.cos(0.5*x))
plt.show()
