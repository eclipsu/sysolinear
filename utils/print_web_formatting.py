from fractions import Fraction

def format_equation(coefficients, constants):
    num_variables = len(constants)
    equations = []
    for i in range(num_variables):
        equation = ""
        for j in range(num_variables):
            variable = chr(ord('a') + j)
            equation += f"{int(coefficients[i][j])}{variable} + "
        equation = equation[:-2]  # Remove the last '+'
        equations.append(f"{equation} = {constants[i]}")
    return equations

def format_solution(solutions):
    formatted_solutions = []
    for i in range(len(solutions)):
        variable = chr(ord('a') + i)
        formatted_solutions.append(f"{variable} = {str(Fraction(solutions[i]).limit_denominator())}")
    return formatted_solutions
