import threading
from fractions import Fraction

# csv imports
import csv
from lib.generate_system import generate_system
from lib.read_equations import read_equations, append_to_csv

# Random System generation
from utils.generate_equations import generate_equations

# Print utils
from utils.print_equation import print_equation
from utils.print_solution import print_solution

# Numerical method functions
from methods.cramers_rule import cramer_rule
from methods.matrix_inversion import matrix_inversion
from methods.row_ech import gauss_jordan_elimination


def run_method(method_name, method_func, coefficients, constants, results_lock):
    solution, execution_time, error = method_func(coefficients, constants)
    fraction_solution = [str(Fraction(element).limit_denominator()) for element in solution]
    with results_lock:
        results[method_name] = (fraction_solution, execution_time, error)


size_unknown = input("Pick the number of unknowns: ")
size_system = input("Pick the number of systems: ")

generate_system(num_variables=int(size_unknown), num_systems=int(size_system), filename='equations.csv')  # Generating
print(f"Successfully generated {size_system} system(s) of {size_unknown} unknowns.")

# Example usage:
input_filename = 'equations.csv'
output_filename_template = 'result_{}_all_systems.csv'

coefficients, constants = read_equations(input_filename)

# Using a thread-safe dictionary to store results for each method
results = {}
results_lock = threading.Lock()

def run_and_update(method_name, method_func, coefficients, constants, index):
    solution, execution_time, error = method_func(coefficients, constants)
    fraction_solution = [str(Fraction(element).limit_denominator()) for element in solution]
    
    with results_lock:
        results[method_name] = (fraction_solution, execution_time, error)
        append_to_csv(output_filename_template.format(method_name), index + 1, coefficients, constants, fraction_solution, error, execution_time)


for index, x in enumerate(coefficients):
    # Create threads for each method
    t1 = threading.Thread(target=run_and_update, args=("Cramer's Rule", cramer_rule, coefficients[index], constants[index], index))
    # t2 = threading.Thread(target=run_and_update, args=("Matrix Inversion", matrix_inversion, coefficients[index], constants[index], index))
    t3 = threading.Thread(target=run_and_update, args=("Row equivalent", gauss_jordan_elimination, coefficients[index], constants[index], index))

    # Start the threads
    t1.start()
    t3.start()
    # t2.start()

    print("Please wait till all methods finish their calculation")
    # Wait for all threads to finish
    t1.join()
    t3.join()
    # t2.join()
    print("Finished!: ")

    # Retrieve and print results (if needed)
    with results_lock:
        for method, (solution, execution_time, error) in results.items():
            print(f"Method: {method}")
            print(f"Solution: {solution}")
            print(f"Error: {error}")
            print(f"Execution time: {execution_time} seconds")
            print()
