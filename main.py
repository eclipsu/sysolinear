import time
import matplotlib.pyplot as plt
import json
import os

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

MEMO_FILE = "memo.json"

def load_memo():
    """Load memoized data from JSON file if it exists and is valid."""
    if os.path.exists(MEMO_FILE):
        try:
            with open(MEMO_FILE, "r") as file:
                data = file.read().strip()
                return json.loads(data) if data else {}  # Handle empty file
        except json.JSONDecodeError:
            print("Warning: Invalid JSON in memo file. Resetting memo.")
            return {}  # Reset memo if corrupted
    return {}

def save_memo(memo):
    """Save updated memoized data to JSON file."""
    with open(MEMO_FILE, "w") as file:
        json.dump(memo, file, indent=4)

def benchmark_methods(max_size):
    sizes = []
    cramer_times = []
    inversion_times = []
    gauss_jordan_times = []

    memo = load_memo()

    for size in range(2, max_size + 1):
        if str(size) in memo and all(key in memo[str(size)] for key in ["cramer", "inversion", "gauss_jordan"]):
            print(f"Skipping computation for size {size}, using cached data.")
            sizes.append(size)
            cramer_times.append(memo[str(size)]["cramer"])
            inversion_times.append(memo[str(size)]["inversion"])
            gauss_jordan_times.append(memo[str(size)]["gauss_jordan"])
            continue 

        coefficients, constants = generate_equations(size)
        # print_equation(coefficients, constants)

        # Initialize or update the memo entry for this size
        if str(size) not in memo:
            memo[str(size)] = {}

        # Benchmark Matrix Inversion
        start_time = time.time()
        inversion_solution = matrix_inversion(coefficients, constants)
        inversion_time = time.time() - start_time
        inversion_times.append(inversion_time)
        memo[str(size)]["inversion"] = inversion_time

        # Benchmark Cramer's Rule
        start_time = time.time()
        cramer_solution = cramer_rule(coefficients, constants)
        cramer_time = time.time() - start_time
        cramer_times.append(cramer_time)
        memo[str(size)]["cramer"] = cramer_time

        # Benchmark Gauss-Jordan Elimination
        start_time = time.time()
        gauss_jordan_solution = gauss_jordan_elimination(coefficients, constants)
        gauss_jordan_time = time.time() - start_time
        gauss_jordan_times.append(gauss_jordan_time)
        memo[str(size)]["gauss_jordan"] = gauss_jordan_time

        # Save updated memo
        save_memo(memo)

        sizes.append(size)

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
    if sizes:
        plot_benchmark_results(sizes, cramer_times, inversion_times, gauss_jordan_times)
