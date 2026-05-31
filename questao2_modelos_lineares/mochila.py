from ortools.linear_solver import pywraplp

def main():
    # Cria o solver para Programação Linear Inteira (SCIP)
    solver = pywraplp.Solver.CreateSolver('SCIP')
    if not solver:
        return

    # Dados do problema
    n = 10
    W = 15
    v = [10, 40, 30, 50, 35, 40, 30, 45, 25, 20]
    w = [1, 3, 4, 5, 2, 3, 2, 4, 1, 2]

    # Variáveis de decisão: Booleanas (0 ou 1) para cada item
    x = [solver.BoolVar(f'x{i}') for i in range(n)]

    # Função Objetivo: Maximizar o valor
    solver.Maximize(sum(v[i] * x[i] for i in range(n)))

    # Restrição: Peso total não pode exceder W
    solver.Add(sum(w[i] * x[i] for i in range(n)) <= W)

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Resposta (Valor Máximo): {solver.Objective().Value()}")
        selecionados = [i+1 for i in range(n) if x[i].solution_value() > 0.5]
        print(f"Itens selecionados: {selecionados}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()