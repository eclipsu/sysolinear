def evaluate_equation(coefficients, values):
    return sum(c * v for c, v in zip(coefficients, values))

# utils/error.py

def calculate_error(coefficients, expected_result, solution):
    result = evaluate_equation(coefficients, solution)
    error = abs(result - expected_result)
    return error


