import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
    return x**3 - 2*x

# Generate a range of x values
x = np.linspace(-3, 3, 400)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(x, f(x), label='y = x^3 - 2x')
plt.title('Graph of y = x^3 - 2x')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
