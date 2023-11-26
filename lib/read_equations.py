import csv
import time
import numpy as np

from utils.print_equation import print_equation
from utils.print_solution import print_solution
from methods.row_ech import gauss_jordan_elimination
from methods.cramers_rule import cramer_rule

def read_equations(filename):
    coefficients_list = []
    constants_list = []

    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        current_system = None
        current_coefficients = []
        current_constants = []

        for row in reader:
            system_num = int(row['System'])
            coefficients = [int(row[f'{chr(ord("a") + i)}']) for i in range(len(row) - 2)]
            constants = int(row['Constants'])

            if current_system is None:
                current_system = system_num

            if system_num == current_system:
                current_coefficients.append(coefficients)
                current_constants.append(constants)
            else:
                coefficients_list.append(current_coefficients)
                constants_list.append(current_constants)
                current_coefficients = [coefficients]
                current_constants = [constants]
                current_system = system_num

        if current_coefficients:
            coefficients_list.append(current_coefficients)
            constants_list.append(current_constants)

    return coefficients_list, constants_list

def append_to_csv(filename, system_num, coefficients, constants, solutions, error, time_taken):
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Flatten the coefficients list
        coefficients_flat = [item for sublist in coefficients for item in sublist]

        row = [system_num] + coefficients_flat + [constants[0]] + solutions + [error] + [time_taken]
        writer.writerow(row)


# # Example usage:
# input_filename = 'equations.csv'
# output_filename = 'results.csv'

# coefficients, constants = read_equations(input_filename)

# with open(output_filename, 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     header = ['System'] + [f'{chr(ord("a") + i)}' for i in range(len(coefficients[0][0]))] + ['Constants', 'Solutions', 'Error', 'Time Taken']
#     writer.writerow(header)

# for index, x in enumerate(coefficients):
#     solutions, execution_time, error = cramer_rule(coefficients[index], constants[index])
#     print_equation(coefficients[index], constants[index])
#     print_solution(solutions, 1)

#     append_to_csv(output_filename, index + 1, coefficients[index], constants[index], solutions, error, execution_time)
