def print_solution(solutions):
    print("\nSolutions are:")
    for i in range(len(solutions)):
        variable = chr(ord('a') + i)
        print(f"{variable} = {solutions[i]}")
