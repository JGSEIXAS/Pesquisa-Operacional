from ortools.linear_solver import pywraplp

def main():
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    # Variáveis contínuas
    AMGS = solver.NumVar(0, solver.infinity(), 'AMGS')
    RE = solver.NumVar(0, solver.infinity(), 'RE')

    # Função Objetivo: Maximizar lucro (11*AMGS + 12*RE)
    solver.Maximize(11 * AMGS + 12 * RE)

    # Restrições de matéria-prima
    solver.Add(AMGS + 4 * RE <= 10000) # Carne
    solver.Add(5 * AMGS + 2 * RE <= 30000) # Cereais

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Valor ótimo (Lucro): {solver.Objective().Value():.2f}")
        print(f"AMGS = {AMGS.solution_value():.2f}")
        print(f"RE = {RE.solution_value():.2f}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()