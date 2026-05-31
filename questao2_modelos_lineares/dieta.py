from ortools.linear_solver import pywraplp

def main():
    # Cria o solver para Programação Linear (Variáveis Contínuas)
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return

    # Dados do problema
    a = [1, 0, 2, 2, 1, 2]
    c = [0, 1, 3, 1, 3, 2]
    p = [35, 30, 60, 50, 27, 22]

    # Variáveis de decisão (x >= 0)
    x = [solver.NumVar(0, solver.infinity(), f'x{i}') for i in range(6)]

    # Função Objetivo: Minimizar custos
    solver.Minimize(sum(x[i] * p[i] for i in range(6)))

    # Restrições de vitaminas mínimas
    solver.Add(sum(x[i] * a[i] for i in range(6)) >= 9)
    solver.Add(sum(x[i] * c[i] for i in range(6)) >= 19)

    # Resolve e imprime os resultados
    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Valor ótimo (Custo): {solver.Objective().Value():.2f}")
        for i in range(6):
            print(f"Ingrediente {i+1}: {x[i].solution_value():.2f}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()