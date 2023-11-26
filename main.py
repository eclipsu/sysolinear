import time

# Random System generation
from utils.generate_equations import generate_equations

# Print utils
from utils.print_equation import print_equation
from utils.print_solution import print_solution

# Numerical method functions
from methods.cramers_rule import cramer_rule
from methods.matrix_inversion import matrix_inversion
from methods.row_ech import gauss_jordan_elimination

from utils.error import calculate_error

size = input("Pick the number of unknowns: ")

coefficients, constants = generate_equations(size) # Generating

print_equation(coefficients, constants)
method_choice = input("Choose the method to solve the linear system:\n1 for Cramer's Rule\n2 for Matrix Inversion\n3 for Row Equivalent\n\nEnter choice: ")

if method_choice == '1':
    solution, execution_time, error = cramer_rule(coefficients, constants)

    print_solution(solution, selected=0)
    print(f"Error: {error}")
    print(f"Execution time: {execution_time} seconds")

elif method_choice == '2':
    solution, execution_time, error = matrix_inversion(coefficients, constants)

    print_solution(solution, selected=1)
    print(f"Error: {error}")
    print(f"Execution time: {execution_time} seconds")
    

elif method_choice == '3':
    # step_choice = input("Show steps?\n1 for Yes\n2 for No\nEnter choice:")
    # steps = True if step_choice == '1' else False

    solution, execution_time, error = gauss_jordan_elimination(coefficients, constants)

    print_solution(solution, selected=2)
    print(f"Error: {error}")
    print(f"Execution time: {execution_time} seconds")

else:
    print("Something went wrong!")
