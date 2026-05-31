from ortools.linear_solver import pywraplp

def main():
    # GLOP para problemas de transporte contínuos
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # Custos de envio (Fábrica i -> Depósito j)
    C = [
        [8,  5,  6],
        [15, 10, 12],
        [3,  9, 10]
    ]
    # Capacidade das fábricas (Oferta)
    F = [120, 80, 80]
    # Demanda dos depósitos
    D = [150, 70, 60]

    # Variáveis: quantidade transportada de i para j (>= 0)
    X = [[solver.NumVar(0, solver.infinity(), f'x_{i}_{j}') for j in range(3)] for i in range(3)]

    # Função Objetivo: Minimizar custos de transporte
    solver.Minimize(sum(X[i][j] * C[i][j] for i in range(3) for j in range(3)))

    # Restrições de Oferta (Fábricas)
    for i in range(3):
        solver.Add(sum(X[i][j] for j in range(3)) <= F[i])

    # Restrições de Demanda (Depósitos)
    for j in range(3):
        solver.Add(sum(X[i][j] for i in range(3)) == D[j])

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Custo ótimo de transporte: {solver.Objective().Value():.2f}")
        for i in range(3):
            for j in range(3):
                val = X[i][j].solution_value()
                if val > 0:
                    print(f"Fábrica {i+1} -> Depósito {j+1}: {val:.2f} unidades")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()