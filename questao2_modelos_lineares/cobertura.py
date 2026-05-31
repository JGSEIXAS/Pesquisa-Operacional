from ortools.linear_solver import pywraplp

def main():
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    n = 5
    # Lista de adjacência
    adj = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 4],
        3: [1],
        4: [2]
    }

    # Variável Booleana: 1 se construímos escola no bairro i
    x = [solver.BoolVar(f'x{i}') for i in range(n)]

    # Função Objetivo: Minimizar o número de escolas construídas
    solver.Minimize(sum(x[i] for i in range(n)))

    # Restrição: Todo bairro u deve ter uma escola ou um vizinho com escola
    for u in range(n):
        vizinhanca = [x[u]] + [x[v] for v in adj[u]]
        solver.Add(sum(vizinhanca) >= 1)

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Número mínimo de escolas: {int(solver.Objective().Value())}")
        escolas = [i+1 for i in range(n) if x[i].solution_value() > 0.5]
        print(f"Construir nos bairros: {escolas}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()