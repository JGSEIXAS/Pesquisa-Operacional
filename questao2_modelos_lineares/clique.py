from docplex.mp.model import Model

def main():
    mdl = Model(name='clique_maxima')
         
    # Grafo de exemplo
    n = 5
    adj = [
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ]
    
    # Variável Booleana
    x = [mdl.binary_var(name=f'x{i}') for i in range(n)]
    
    # Função Objetivo
    mdl.maximize(mdl.sum(x[i] for i in range(n)))
    
    # Restrição
    for i in range(n):
        for j in range(i + 1, n):
            if adj[i][j] == 0:
                mdl.add_constraint(x[i] + x[j] <= 1)
                
    solution = mdl.solve()
    if solution:
        print(f"Tamanho da Clique Máxima: {int(mdl.objective_value)}")
        clique = [i+1 for i in range(n) if x[i].solution_value > 0.5]
        print(f"Vértices na clique: {clique}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()