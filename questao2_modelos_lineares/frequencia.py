from ortools.linear_solver import pywraplp

def main():
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    n = 4 # Número de antenas (vértices)
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)] # Grafo de interferência

    # Variáveis
    # X[i][c] = 1 se a antena i usa a frequência c (no máximo temos n cores)
    X = [[solver.BoolVar(f'x_{i}_{c}') for c in range(n)] for i in range(n)]
    # y[c] = 1 se a frequência c está a ser utilizada por alguma antena
    y = [solver.BoolVar(f'y{c}') for c in range(n)]

    # Função Objetivo: Minimizar o número total de frequências usadas
    solver.Minimize(sum(y[c] for c in range(n)))

    # Restrições
    for i in range(n):
        # Cada antena deve ter exatamente 1 frequência
        solver.Add(sum(X[i][c] for c in range(n)) == 1)

    for u, v in edges:
        for c in range(n):
            # Antenas com interferência não podem usar a mesma frequência
            # E força y[c] a ser 1 se a frequência c for usada por u ou v
            solver.Add(X[u][c] + X[v][c] <= y[c])

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Número mínimo de frequências (cores): {int(solver.Objective().Value())}")
        for i in range(n):
            for c in range(n):
                if X[i][c].solution_value() > 0.5:
                    print(f"Antena {i+1}: usa Frequência {c+1}")
                    break
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()