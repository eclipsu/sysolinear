# utils/print_equation.py

def print_equation(coefficients, constants):
    num_variables = len(constants)
    print("\nThe equations are:")
    for i in range(num_variables):
        equation = ""
        for j in range(num_variables):
            variable = chr(ord('a') + j)
            equation += f"{coefficients[i][j]}{variable} + "
        equation = equation[:-2]  # Remove the last '+'
        print(f"{equation} = {constants[i]}")
    print("\n")
