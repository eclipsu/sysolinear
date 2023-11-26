import threading
from fractions import Fraction


# Random System generation
from utils.generate_equations import generate_equations

# Print utils
from utils.print_equation import print_equation
from utils.print_solution import print_solution

# Numerical method functions
from methods.cramers_rule import cramer_rule
from methods.matrix_inversion import matrix_inversion
from methods.row_ech import gauss_jordan_elimination


def run_method(method_func, coefficients, constants):
    solution, execution_time, error = method_func(coefficients, constants)
    fraction_solution = [str(Fraction(element).limit_denominator()) for element in solution]
    return fraction_solution, execution_time, error

size = input("Pick the number of unknowns: ")

coefficients, constants = generate_equations(size)  # Generating

print_equation(coefficients, constants)
print()

# Using a thread-safe dictionary to store results for each method
results = {}
results_lock = threading.Lock()

def run_and_update(method_name, method_func, coefficients, constants):
    result = run_method(method_func, coefficients, constants)
    with results_lock:
        results[method_name] = result

# Create threads for each method
t1 = threading.Thread(target=run_and_update, args=("Cramer's Rule", cramer_rule, coefficients, constants))
t2 = threading.Thread(target=run_and_update, args=("Matrix Inversion", matrix_inversion, coefficients, constants))
t3 = threading.Thread(target=run_and_update, args=("Row equivalent", gauss_jordan_elimination, coefficients, constants))

# Start the threads
t1.start()
t3.start()
t2.start()

print("Please wait till all methods finish their calculation")
# Wait for all threads to finish
t1.join()
t3.join()
t2.join()
print("Finished!: ")

# Retrieve and print results
with results_lock:
    for method, (solution, execution_time, error) in results.items():
        print(f"Method: {method}")
        print(f"Solution: {solution}")
        print(f"Error: {error}")
        print(f"Execution time: {execution_time} seconds")
        print()
