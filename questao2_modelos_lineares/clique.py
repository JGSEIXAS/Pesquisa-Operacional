from ortools.linear_solver import pywraplp

def main():
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Grafo de exemplo
    n = 5
    # Matriz de adjacência (1 se existe aresta, 0 caso contrário)
    adj = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]

    # Variável Booleana: 1 se o vértice i pertence à clique
    x = [solver.BoolVar(f'x{i}') for i in range(n)]

    # Função Objetivo: Maximizar o número de vértices na clique
    solver.Maximize(sum(x[i] for i in range(n)))

    # Restrição: Se não existe aresta entre i e j, ambos não podem estar na clique
    for i in range(n):
        for j in range(i + 1, n): # Evita duplicação e comparações i==j
            if adj[i][j] == 0:
                solver.Add(x[i] + x[j] <= 1)

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Tamanho da Clique Máxima: {int(solver.Objective().Value())}")
        clique = [i+1 for i in range(n) if x[i].solution_value() > 0.5]
        print(f"Vértices na clique: {clique}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()