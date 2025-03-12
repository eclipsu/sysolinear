import time
import matplotlib.pyplot as plt

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

def benchmark_methods(max_size):
    sizes = range(2, max_size + 1)
    cramer_times = []
    inversion_times = []
    gauss_jordan_times = []

    for size in sizes:
        coefficients, constants = generate_equations(size)

        # Benchmark Cramer's Rule
        start_time = time.time()
        cramer_rule(coefficients, constants)
        cramer_times.append(time.time() - start_time)

        # Benchmark Matrix Inversion
        start_time = time.time()
        matrix_inversion(coefficients, constants)
        inversion_times.append(time.time() - start_time)

        # Benchmark Gauss-Jordan Elimination
        start_time = time.time()
        gauss_jordan_elimination(coefficients, constants)
        gauss_jordan_times.append(time.time() - start_time)

    return sizes, cramer_times, inversion_times, gauss_jordan_times

def plot_benchmark_results(sizes, cramer_times, inversion_times, gauss_jordan_times):
    plt.plot(sizes, cramer_times, label="Cramer's Rule")
    plt.plot(sizes, inversion_times, label="Matrix Inversion")
    plt.plot(sizes, gauss_jordan_times, label="Gauss-Jordan Elimination")
    plt.xlabel('Size of the System')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Benchmarking of Linear System Solvers')
    plt.legend()
    plt.grid(True)
    plt.show()

# Main code
if __name__ == "__main__":
    max_size = int(input("Enter the maximum size of the system for benchmarking: "))
    sizes, cramer_times, inversion_times, gauss_jordan_times = benchmark_methods(max_size)
    plot_benchmark_results(sizes, cramer_times, inversion_times, gauss_jordan_times)