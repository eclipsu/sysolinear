from fractions import Fraction

methods = ["Cramer's rule", "Matrix Inversion", "Row Equivalent"]

def print_solution(solutions, selected):
    print(f"\nBy using {methods[selected]}:")
    for i in range(len(solutions)):
        variable = chr(ord('a') + i)
        print(f"{variable} = {str(Fraction(solutions[i]).limit_denominator())}")


        
