"""## Question 2: Implementing Box-Muller Transformation algorithm"""

import numpy as np
import matplotlib.pyplot as plt

def gaussianTransform(x, y):
  x_new = np.sqrt(-2*np.log(x))*np.cos(2*np.pi*y)
  y_new = np.sqrt(-2*np.log(x))*np.sin(2*np.pi*y)

  return x_new, y_new

x_u = np.random.rand(5000)
y_u = np.random.rand(5000)

x_g, y_g = gaussianTransform(x_u, y_u)

fig = plt.figure()

plt.subplot(2, 2, 1)
plt.hist(x_u, ec='black')

plt.subplot(2, 2, 2)
plt.hist(y_u, ec='black')

plt.subplot(2, 2, 3)
plt.hist(x_g, ec='black')

plt.subplot(2, 2, 4)
plt.hist(y_g, ec='black')

plt.show()