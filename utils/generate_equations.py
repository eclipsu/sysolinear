import numpy as np

def generate_equations(size):
    if int(size) <= 0 or int(size) > 26:
        size = 2

    while True:
        # Generate random coefficients and constants
        coefficients = np.random.randint(1, 10, size=(int(size), int(size)))
        constants = np.random.randint(1, 10, size=int(size))

        is_solvable = np.linalg.det(coefficients) != 0

        if is_solvable:
            return coefficients.tolist(), constants.tolist()

