import numpy as np
import matplotlib.pyplot as plt

# Define the time values
t_values = np.linspace(0, 50, 500)  # Adjust the range and number of points as needed

# Calculate y values using the given function
y_values = (np.exp(-t_values/8) / (8 * np.sqrt(15))) * (9 * np.sin(np.sqrt(15) * t_values / 8) - np.sqrt(15) * np.cos(np.sqrt(15) * t_values / 8))

# Plot the graph
plt.plot(t_values, y_values, label=r'$\frac{e^{-t/8}}{8\sqrt{15}} \left(9\sin\left(\frac{\sqrt{15}t}{8}\right) - \sqrt{15}\cos\left(\frac{\sqrt{15}t}{8}\right)\right)$')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)
plt.savefig('b.png')

