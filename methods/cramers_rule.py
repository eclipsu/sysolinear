# methods/cramers_rule.py
from utils.print_solution import print_solution
from utils.print_equation import print_equation

def calculate_determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Parameters:
    - matrix: A square matrix represented as a list of lists.

    Returns:
    - determinant: The determinant of the matrix.
    """
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for i in range(size):
            det += ((-1) ** i) * matrix[0][i] * calculate_determinant(submatrix(matrix, i))
        return det

def submatrix(matrix, col):
    """
    Get the submatrix obtained by removing the first row and the specified column from a matrix.

    Parameters:
    - matrix: A matrix represented as a list of lists.
    - col: The index of the column to be removed.

    Returns:
    - submatrix: The submatrix with the first row and specified column removed.
    """
    return [row[:col] + row[col + 1:] for row in matrix[1:]]

def cramer_rule(coefficients, constants):
    """
    Solve a system of linear equations using Cramer's Rule.

    Parameters:
    - coefficients: Coefficient matrix represented as a list of lists.
    - constants: Constants matrix represented as a list.

    Returns:
    - solutions: A list containing the solutions for each variable.
    """

    # Check if the coefficient matrix is square
    size = len(coefficients)
    if size != len(coefficients[0]):
        raise ValueError("Coefficient matrix must be square for Cramer's Rule")

    # Check if the determinant of the coefficient matrix is zero
    det_coeff = calculate_determinant(coefficients)
    if det_coeff == 0:
        raise ValueError("Determinant of the coefficient matrix is zero. Cramer's Rule is not applicable.")

    num_variables = len(constants)
    solutions = [0] * num_variables

    # Solve the system using Cramer's Rule
    for i in range(num_variables):
        # Create a copy of the coefficient matrix and replace the i-th column with the constants
        temp_matrix = [row.copy() for row in coefficients]
        for j in range(num_variables):
            temp_matrix[j][i] = constants[j]

        # Calculate the determinant of the modified matrix
        det_temp = calculate_determinant(temp_matrix)

        # Calculate the solution for the i-th variable
        solutions[i] = det_temp / det_coeff

    return solutions
