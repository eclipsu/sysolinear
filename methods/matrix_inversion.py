from utils.print_equation import print_equation
from utils.print_solution import print_solution

def transpose(matrix):
    """
    Calculate the transpose of a matrix.

    Parameters:
    - matrix: A matrix represented as a list of lists.

    Returns:
    - transposed_matrix: The transpose of the matrix.
    """
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_multiply(matrix1, matrix2):
    """
    Multiply two matrices.

    Parameters:
    - matrix1: First matrix represented as a list of lists.
    - matrix2: Second matrix represented as a list of lists.

    Returns:
    - result_matrix: The result of the matrix multiplication.
    """
    return [[sum(a * b for a, b in zip(row, col)) for col in transpose(matrix2)] for row in matrix1]

def matrix_inverse(matrix):
    """
    Calculate the inverse of a square matrix.

    Parameters:
    - matrix: A square matrix represented as a list of lists.

    Returns:
    - inverse_matrix: The inverse of the matrix.
    """
    size = len(matrix)
    identity_matrix = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

    # Forward elimination
    for i in range(size):
        # Normalize the pivot row
        factor = matrix[i][i]
        for j in range(size):
            matrix[i][j] /= factor
            identity_matrix[i][j] /= factor

        # Eliminate other rows
        for k in range(size):
            if k != i:
                factor = matrix[k][i]
                for j in range(size):
                    matrix[k][j] -= factor * matrix[i][j]
                    identity_matrix[k][j] -= factor * identity_matrix[i][j]

    return identity_matrix

def matrix_inversion(coefficients, constants):
    """
    Solve a system of linear equations using matrix inversion.

    Parameters:
    - coefficients: Coefficient matrix represented as a list of lists.
    - constants: Constants matrix represented as a list.

    Returns:
    - solutions: A list containing the solutions for each variable.
    """

    inverse_coefficients = matrix_inverse(coefficients)
    solutions = matrix_multiply(inverse_coefficients, [[constant] for constant in constants])

    return [s[0] for s in solutions]
