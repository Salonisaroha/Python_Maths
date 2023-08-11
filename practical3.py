import matplotlib.pyplot  as plt
import numpy as np
x = np.linspace(-10, 10, 10)
y = x**2
z = y**2
plt.plot(x, y, color = "blue")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph")
plt.show()
