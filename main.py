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

size = input("Pick the number of unknowns: ")

coefficients, constants = generate_equations(size) # Generating

print_equation(coefficients, constants)
method_choice = input("Choose the method to solve the linear system:\n1 for Cramer's Rule\n2 for Matrix Inversion\n3 for Row Equivalent\n\nEnter choice: ")

if method_choice == '1':
    # Measure the execution time of cramer_rule function
    start_time = time.time()
    solution = cramer_rule(coefficients, constants)
    end_time = time.time()

    print("Using Cramer's Rule:")
    print_solution(solution)

    print(f"Execution time: {end_time - start_time} seconds")

elif method_choice == '2':
    start_time = time.time()
    solution = matrix_inversion(coefficients, constants)
    end_time = time.time()

    print("\nUsing Matrix Inversion method:")
    print_solution(solution)

    print(f"Execution time: {end_time - start_time} seconds")
    

elif method_choice == '3':
    step_choice = input("Show steps?\n1 for Yes\n2 for No\n Enter choice:")
    steps = True if step_choice == '1' else False

    start_time = time.time()
    solution = gauss_jordan_elimination(coefficients, constants, steps=steps)
    end_time = time.time()

    print("\nUsing Row reduction method:")
    print_solution(solution)

    print(f"Execution time: {end_time - start_time} seconds")

else:
    print("Something went wrong!")
