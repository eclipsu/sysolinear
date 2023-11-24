from fractions import Fraction
from utils.print_equation import print_equation
from utils.print_solution import print_solution

def print_matrix(matrix):
    """
    Print a matrix.

    Parameters:
    - matrix: A matrix represented as a list of lists.
    """
    for row in matrix:
        print([str(Fraction(element).limit_denominator()) for element in row])

def gauss_jordan_elimination(coefficients, constants, steps=False):
    """
    Solve a system of linear equations using Gauss-Jordan Elimination with logging.

    Parameters:
    - coefficients: Coefficient matrix represented as a list of lists.
    - constants: Constants matrix represented as a list.
    - steps: A boolean flag indicating whether to print steps or not. Default is False.

    Returns:
    - solutions: A list containing the solutions for each variable.
    """
    augmented_matrix = [coefficients[i] + [constants[i]] for i in range(len(constants))]
    num_variables = len(constants)

    if(steps==True):
        # Print initial augmented matrix
        print("Initial Augmented Matrix:")
        print_matrix(augmented_matrix)
        print("\n")

    for i in range(num_variables):
        # Pivot row
        pivot_row = i

        # Find the pivot row (the row with the largest absolute value in the current column)
        for j in range(i + 1, num_variables):
            if abs(augmented_matrix[j][i]) > abs(augmented_matrix[pivot_row][i]):
                pivot_row = j

        # Swap the current row with the pivot row
        augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]
        if steps:
            print(f"R{i+1} <-> R{pivot_row+1}")

        # Scale the pivot row to make the pivot element 1
        pivot_element = augmented_matrix[i][i]
        for j in range(i, num_variables + 1):
            augmented_matrix[i][j] /= pivot_element
        if steps:
            print(f"R{i+1} * 1/{pivot_element}")

        # Eliminate other rows
        for k in range(num_variables):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(i, num_variables + 1):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]
                if steps:
                    print(f"R{k+1} -> R{k+1} - ({factor}) * R{i+1}")

        # Print the current augmented matrix
        if steps:
            print(f"Step {i + 1}:")
            print_matrix(augmented_matrix)
            print("\n")

    # Extract solutions
    solutions = [row[-1] for row in augmented_matrix]

  

    return solutions
