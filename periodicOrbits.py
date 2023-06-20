import numpy as np
import matplotlib.pyplot as plt

def logistic_map(x, r):
    return r * x * (1 - x)

def find_periodic_orbits(x0, r, n_iterations):
    orbit = [x0]
    for _ in range(n_iterations):
        x = logistic_map(orbit[-1], r)
        if x in orbit:
            break
        orbit.append(x)
    return orbit

# Parameters
x0 = 0.4  # Initial value
r = 3.8   # Control parameter
n_iterations = 1000  # Number of iterations

# Generate periodic orbit
orbit = find_periodic_orbits(x0, r, n_iterations)

# Plotting
fig, ax = plt.subplots()
ax.plot(orbit, 'b-', label='Orbit')
ax.set_xlabel('Iteration')
ax.set_ylabel('Value')
ax.set_title('Dense Periodic Orbit')
plt.legend()
plt.show()
