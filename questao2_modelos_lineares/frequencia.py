from docplex.mp.model import Model

def main():
    mdl = Model(name='alocacao_frequencias')
         
    n = 4 
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)] 
    
    X = [[mdl.binary_var(name=f'x_{i}_{c}') for c in range(n)] for i in range(n)]
    y = [mdl.binary_var(name=f'y{c}') for c in range(n)]
    
    mdl.minimize(mdl.sum(y[c] for c in range(n)))
    
    for i in range(n):
        mdl.add_constraint(mdl.sum(X[i][c] for c in range(n)) == 1)
        
    for u, v in edges:
        for c in range(n):
            mdl.add_constraint(X[u][c] + X[v][c] <= y[c])
            
    solution = mdl.solve()
    if solution:
        print(f"Número mínimo de frequências (cores): {int(mdl.objective_value)}")
        for i in range(n):
            for c in range(n):
                if X[i][c].solution_value > 0.5:
                    print(f"Antena {i+1}: usa Frequência {c+1}")
                    break
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()