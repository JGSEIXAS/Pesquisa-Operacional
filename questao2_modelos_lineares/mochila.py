from docplex.mp.model import Model

def main():
    mdl = Model(name='problema_da_mochila')
    
    n = 10
    W = 15
    v = [10, 40, 30, 50, 35, 40, 30, 45, 25, 20]
    w = [1, 3, 4, 5, 2, 3, 2, 4, 1, 2]
    
    x = [mdl.binary_var(name=f'x{i}') for i in range(n)]
    
    mdl.maximize(mdl.sum(v[i] * x[i] for i in range(n)))
    mdl.add_constraint(mdl.sum(w[i] * x[i] for i in range(n)) <= W)
    
    solution = mdl.solve()
    if solution:
        print(f"Resposta (Valor Máximo): {mdl.objective_value}")
        selecionados = [i+1 for i in range(n) if x[i].solution_value > 0.5]
        print(f"Itens selecionados: {selecionados}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()