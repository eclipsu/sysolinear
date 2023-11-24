from methods.cramers_rule import cramer_rule
from methods.matrix_inversion import matrix_inversion
from methods.row_ech import gauss_jordan_elimination
from utils.print_equation import print_equation
from utils.print_solution import print_solution

# Example coefficients and constants
coefficients = [[2, 3, 1], [3, -2, 4], [1, 1, 1]]
constants = [10, 4, 6]

print_equation(coefficients, constants)
method_choice = input("Choose the method to solve the linear system:\n1 for Cramer's Rule\n2 for Matrix Inversion\n3 for Row Equivalent\n\nEnter choice: ")

if method_choice == '1':
    # Display the solutions using the new print_solution function
    print("Using Cramers Rule:")
    print_solution(cramer_rule(coefficients, constants))

elif method_choice == '2':
    print("Using Matrix Inversion method:")
    print_solution(matrix_inversion(coefficients, constants))

elif method_choice == '3':
    step_choice = input("Show steps?\n1 for Yes\n2 for No\n Enter choice:")
    steps = True if step_choice == '1' else False
    print("Using Row reduction method:")
    print_solution(gauss_jordan_elimination(coefficients, constants, steps=steps))
else:
    print("Something went wrong!")

# Call the function
# solutions = cramer_rule(coefficients, constants)
# matrix_inversion(coefficients, constants)
# gauss_jordan_elimination(coefficients, constants)