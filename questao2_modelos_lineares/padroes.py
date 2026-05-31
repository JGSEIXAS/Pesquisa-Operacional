from ortools.linear_solver import pywraplp

def main():
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return

    # Variáveis Inteiras: Quantidade de folhas de cada padrão e total de latas (y)
    x1 = solver.IntVar(0, solver.infinity(), 'x1')
    x2 = solver.IntVar(0, solver.infinity(), 'x2')
    x3 = solver.IntVar(0, solver.infinity(), 'x3')
    x4 = solver.IntVar(0, solver.infinity(), 'x4')
    y = solver.IntVar(0, solver.infinity(), 'y')

    # Função Objetivo: Maximizar o lucro
    # Lucro = Venda (50*y) - Estocagem_Corpos - Estocagem_Tampas
    solver.Maximize(
        50 * y 
        - 5 * (x1 + 2 * x2 + 4 * x4 - y) 
        - 3 * (7 * x1 + 3 * x2 + 9 * x3 + 4 * x4 - 2 * y)
    )

    # Restrições de disponibilidade de chapas
    solver.Add(x1 + x3 + x4 <= 200) # Chapas de tamanho 1
    solver.Add(x2 <= 90)            # Chapas de tamanho 2

    # Restrições de produção de latas
    solver.Add(y <= (x1 + 2 * x2 + 4 * x4)) # Limite de corpos
    solver.Add(y <= (7 * x1 + 3 * x2 + 9 * x3 + 4 * x4) / 2) # Limite de tampas (2 por lata)

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Valor ótimo (Lucro): {solver.Objective().Value():.2f}")
        print(f"Total de latas produzidas: {int(y.solution_value())}")
        print(f"Padrão 1: {int(x1.solution_value())}")
        print(f"Padrão 2: {int(x2.solution_value())}")
        print(f"Padrão 3: {int(x3.solution_value())}")
        print(f"Padrão 4: {int(x4.solution_value())}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()