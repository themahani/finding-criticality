import numpy as np
from matplotlib import pyplot as plt

N = 500

data = np.load('N1000 j1.5 d1.5 g7.0 w1.975 base5 PA_Hei_pos.npy')

x = np.arange(data[0],data[0]+len(data)-1)
y = data[1:]

plt.loglog()
z = (y != 0)

plt.scatter(x[z], y[z]/y.sum(), s=5)
plt.show()
