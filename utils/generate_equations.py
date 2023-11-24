import numpy as np

# Define the size of the system (number of variables)
n = 4

# Generate random coefficients and constants
coefficients = np.random.randint(1, 10, size=(n, n))
constants = np.random.randint(1, 10, size=n)

# Display the generated system
print(f'coefficients = {coefficients.tolist()}')
print(f'constants = {constants.tolist()}')

# Check if the system is solvable
is_solvable = np.linalg.det(coefficients) != 0

print("\nIs the system solvable?", is_solvable)
