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

# size = input("Pick the number of unknowns: ")

# coefficients, constants = generate_equations(size) # Generating
# print(coefficients, constants)

coefficients, constants = [[60, -48, -88, -9, -25, 54, 24, -31, 90, 24], [-16, 18, 66, 4, 75, -58, 5, -30, -18, -39], [-32, 99, 13, 76, -88, 74, 84, 67, -52, 28], [28, -80, -4, 18, 75, -44, 5, -56, 47, -44], [-67, 9, 6, -19, 64, -57, 85, -50, 17, 71], [-71, 51, -100, 68, -33, -69, -19, -37, 46, 82], [-66, -84, 21, -8, 95, 22, 56, 
50, 58, -34], [12, 78, 85, 37, 88, -20, 56, 4, 57, 7], [90, -38, 3, -16, 99, 1, -59, 73, 60, -71], [-13, -95, -78, -34, 71, 40, -37, -27, 88, -40]], [-61, 91, -45, -86, -40, -29, 10, -98, 47, 70]

print_equation(coefficients, constants)
print()
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
    
input("Press enter to exit")
