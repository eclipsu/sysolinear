import numpy as np
import csv

def generate_system(num_variables, num_systems=1, filename='equations.csv'):
    num_equations_per_system=num_variables
    if num_variables <= 0 or num_systems <= 0 or num_equations_per_system <= 0:
        return None

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        header = ['System'] + [f'{chr(ord("a") + i)}' for i in range(num_variables)] + ['Constants']
        writer.writerow(header)

        for system_num in range(1, num_systems + 1):
            for equation_num in range(1, num_equations_per_system + 1):
                # Generate random coefficients and constants
                coefficients = np.random.randint(-100, 100, size=num_variables)
                constants = np.random.randint(-100, 100)

                # Ensure coefficients are not all zeros
                while np.all(coefficients == 0):
                    coefficients = np.random.randint(-100, 100, size=num_variables)

                # Write system number
                row = [system_num]

                # Write coefficients
                row.extend(coefficients.tolist())

                # Write constants
                row.append(constants)

                writer.writerow(row)

# Example usage:
# generate_equations(num_variables=2, num_systems=30, filename='equations.csv')
