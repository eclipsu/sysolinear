# Linear System Solvers Benchmarking

This project benchmarks the performance of three numerical methods for solving linear systems of equations:

1. **Cramer's Rule**
2. **Matrix Inversion**
3. **Gauss Jordan Elimination**

The tool generates random systems of equations, solves them using the selected method, and measures execution time and error. It visualizes the results using **Matplotlib**.

---

## Features

- Generates systems of linear equations with customizable sizes.
- Supports Cramer's Rule, Matrix Inversion, and Gauss-Jordan Elimination.
- Measures execution time and calculates error for each method.
- Plots execution times for different system sizes using Matplotlib.
- Uses multiprocessing to speed up benchmarking for large systems.

---

## Installation

### Prerequisites

- Python 3.x
- Required Python libraries: `numpy`, `matplotlib`

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/eclipsu/sysolinear.git
   cd sysolinear
   ```
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the benchmarking tool:

   ```bash
   python main.py
   ```

2. Enter the **maximum size** of the system you want to benchmark:

   ```
   Enter the maximum size of the system for benchmarking: 50
   ```

3. The tool will:

   - Generate random systems of equations.
   - Solve them using all three methods.
   - Display execution times and errors.
   - Plot the results using Matplotlib.

---

## Example Output

for size of 10 :

![Benchmarking of Linear system Solvers for 10 variable system](https://i.imgur.com/tgQ2XAu.png)

---

## File Structure

```
sysolinear/
├── main.py                  # Main script
├── methods/                 # Folder containing numerical methods
│   ├── cramers_rule.py      # Cramer's Rule
│   ├── matrix_inversion.py  # Matrix Inversion
│   └── row_ech.py           # Gauss-Jordan Elimination implementation
├── utils/                   # Utility functions
│   ├── generate_equations.py# Random equation generator
│   ├── print_equation.py    # Function to print equations
│   ├── print_solution.py    # Function to print solutions
│   └── error.py             # Error calculation utility
├── requirements.txt         # List of dependencies
└── README.md                # This file
```

---

## Contribution

There are room for contributions! Thus, contributions are welcomed! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## Acknowledgments

- To my teacher, Durga Prasad Patel, from my Grade 12 Numerical Computation class
