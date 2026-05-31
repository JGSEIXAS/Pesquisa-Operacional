from ortools.linear_solver import pywraplp

def main():
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    d = [5, 7, 6, 8, 4, 7, 5]
    # Matriz de cobertura (turnos de 5 dias seguidos e 3 de folga)
    a = [
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0]
    ]

    # Variáveis inteiras: quantas enfermeiras começam no padrão 's'
    x = [solver.IntVar(0, solver.infinity(), f'x{s}') for s in range(8)]

    # Atender a procura diária
    for i in range(7):
        solver.Add(sum(a[i][s] * x[s] for s in range(8)) >= d[i])

    # Minimizar o total de enfermeiras contratadas
    solver.Minimize(sum(x[s] for s in range(8)))

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Resposta (Total Enfermeiras): {int(solver.Objective().Value())}")
    else:
        print("Sem solução.")

if __name__ == "__main__":
    main()