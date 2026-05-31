from ortools.linear_solver import pywraplp

def main():
    # Para fluxo usamos GLOP pois o fluxo pode ser contínuo
    solver = pywraplp.Solver.CreateSolver('GLOP')
    
    n = 4 # Número de nós
    s = 0 # Fonte
    t = 3 # Sorvedouro
    
    # Matriz de adjacência com capacidades
    adj = [
        [0, 10, 5, 0],
        [0, 0, 15, 10],
        [0, 0, 0, 10],
        [0, 0, 0, 0]
    ]

    # Variáveis de fluxo X[i][j]
    X = [[solver.NumVar(0, adj[i][j], f'x_{i}_{j}') for j in range(n)] for i in range(n)]

    # Função Objetivo: Maximizar o fluxo que chega ao sorvedouro (t)
    solver.Maximize(sum(X[i][t] for i in range(n)))

    # Restrições de conservação de fluxo para nós que não são s nem t
    for v in range(n):
        if v == s or v == t:
            continue
        fluxo_entrando = sum(X[j][v] for j in range(n))
        fluxo_saindo = sum(X[v][j] for j in range(n))
        solver.Add(fluxo_entrando == fluxo_saindo)

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Fluxo Máximo: {solver.Objective().Value()}")
        for i in range(n):
            for j in range(n):
                val = X[i][j].solution_value()
                if val > 0:
                    print(f"Aresta ({i+1} -> {j+1}): {val}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()