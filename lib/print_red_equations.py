# utils/print_equation.py
import math

def sign(num):
    return '-' if num < 0 else '+'

def print_equation(coefficients, constants):
    num_equations, num_variables = coefficients.shape  # Get the shape of coefficients

    print("\nThe equations are:")
    for i in range(num_equations):
        equation = ""
        for j in range(num_variables):
            variable = chr(ord('a') + j)
            
            # Handle the case where coefficients may have a different structure
            if isinstance(coefficients[i], list):
                coefficient = coefficients[i][j]
            else:
                coefficient = coefficients[i, j]

            if coefficient != 0:
                sign_str = sign(coefficient)
                coefficient_str = f"{abs(coefficient)}" if abs(coefficient) != 1 else ""
                equation += f" {sign_str} {coefficient_str}{variable}"

        print(f"{equation} = {constants[i]}")

# Ensure to import this updated function in read_equations.py
