from docplex.mp.model import Model

def main():
    mdl = Model(name='problema_transporte')
          
    C = [
        [8,  5,  6],
        [15, 10, 12],
        [3,  9, 10]
    ]
    F = [120, 80, 80]
    D = [150, 70, 60]
    
    X = [[mdl.continuous_var(lb=0, name=f'x_{i}_{j}') for j in range(3)] for i in range(3)]
    
    mdl.minimize(mdl.sum(X[i][j] * C[i][j] for i in range(3) for j in range(3)))
    
    for i in range(3):
        mdl.add_constraint(mdl.sum(X[i][j] for j in range(3)) <= F[i])
        
    for j in range(3):
        mdl.add_constraint(mdl.sum(X[i][j] for i in range(3)) == D[j])
        
    solution = mdl.solve()
    if solution:
        print(f"Custo ótimo de transporte: {mdl.objective_value:.2f}")
        for i in range(3):
            for j in range(3):
                val = X[i][j].solution_value
                if val > 0:
                    print(f"Fábrica {i+1} -> Depósito {j+1}: {val:.2f} unidades")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()