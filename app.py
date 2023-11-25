# app.py

from flask import Flask, render_template, request
from utils.generate_equations import generate_equations
from utils.print_web_formatting import format_equation, format_solution
from methods.cramers_rule import cramer_rule
from methods.matrix_inversion import matrix_inversion
from methods.row_ech import gauss_jordan_elimination

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    size = request.form['size']
    coefficients, constants = generate_equations(size)

    # Get the chosen method from the form
    method_choice = request.form['method']


    if method_choice == '1':
        solution, execution_time, error = cramer_rule(coefficients, constants)
    elif method_choice == '2':
        solution, execution_time, error = matrix_inversion(coefficients, constants)
    elif method_choice == '3':
        steps = request.form.get('show_steps') == 'on'
        solution, execution_time, error = gauss_jordan_elimination(coefficients, constants, steps=steps)
    else:
        return "Invalid method selected"

    formatted_equations = format_equation(coefficients, constants)
    formatted_solution = format_solution(solution)

    return render_template('result.html', size=size, equations=formatted_equations, method=method_choice, solution=formatted_solution,execution_time=execution_time, error=error)

if __name__ == '__main__':
    app.run(debug=True)
