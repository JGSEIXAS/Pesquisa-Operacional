from docplex.mp.model import Model

def main():
    mdl = Model(name='localizacao_facilidades')
         
    n = 3 
    m = 4 
    f = [100, 150, 120] 
    c = [               
        [10, 20, 30, 40],
        [20, 15, 25, 30],
        [30, 25, 20, 15]
    ]
    
    y = [mdl.binary_var(name=f'y{i}') for i in range(n)]
    X = [[mdl.binary_var(name=f'x_{i}_{j}') for j in range(m)] for i in range(n)]
    
    custo_instalacao = mdl.sum(y[i] * f[i] for i in range(n))
    custo_atendimento = mdl.sum(X[i][j] * c[i][j] for i in range(n) for j in range(m))
    mdl.minimize(custo_instalacao + custo_atendimento)
    
    for j in range(m):
        mdl.add_constraint(mdl.sum(X[i][j] for i in range(n)) == 1)
        for i in range(n):
            mdl.add_constraint(X[i][j] <= y[i])
            
    solution = mdl.solve()
    if solution:
        print(f"Custo ótimo: {mdl.objective_value}")
        for i in range(n):
            if y[i].solution_value > 0.5:
                atendidos = [j+1 for j in range(m) if X[i][j].solution_value > 0.5]
                print(f"Depósito {i+1} instalado. Atende clientes: {atendidos}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()