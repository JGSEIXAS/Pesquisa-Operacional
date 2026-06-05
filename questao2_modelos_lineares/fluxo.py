from docplex.mp.model import Model

def main():
    mdl = Model(name='fluxo_maximo')
         
    n = 4 
    s = 0 
    t = 3 
         
    adj = [
        [0, 10, 5, 0],
        [0, 0, 15, 10],
        [0, 0, 0, 10],
        [0, 0, 0, 0]
    ]
    
    X = [[mdl.continuous_var(lb=0, ub=adj[i][j], name=f'x_{i}_{j}') for j in range(n)] for i in range(n)]
    
    mdl.maximize(mdl.sum(X[i][t] for i in range(n)))
    
    for v in range(n):
        if v == s or v == t:
            continue
        fluxo_entrando = mdl.sum(X[j][v] for j in range(n))
        fluxo_saindo = mdl.sum(X[v][j] for j in range(n))
        mdl.add_constraint(fluxo_entrando == fluxo_saindo)
        
    solution = mdl.solve()
    if solution:
        print(f"Fluxo Máximo: {mdl.objective_value}")
        for i in range(n):
            for j in range(n):
                val = X[i][j].solution_value
                if val > 0:
                    print(f"Aresta ({i+1} -> {j+1}): {val}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()