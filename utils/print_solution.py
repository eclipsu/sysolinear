from fractions import Fraction

def print_solution(solutions):
    for i in range(len(solutions)):
        variable = chr(ord('a') + i)
        print(f"{variable} = {str(Fraction(solutions[i]).limit_denominator())}")


        
