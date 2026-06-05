from docplex.mp.model import Model

def main():
    mdl = Model(name='problema_da_dieta')
    
    a = [1, 0, 2, 2, 1, 2]
    c = [0, 1, 3, 1, 3, 2]
    p = [35, 30, 60, 50, 27, 22]
    
    # Variáveis contínuas (padrão lb=0, ub=+inf)
    x = [mdl.continuous_var(lb=0, name=f'x{i}') for i in range(6)]
    
    mdl.minimize(mdl.sum(x[i] * p[i] for i in range(6)))
    
    mdl.add_constraint(mdl.sum(x[i] * a[i] for i in range(6)) >= 9)
    mdl.add_constraint(mdl.sum(x[i] * c[i] for i in range(6)) >= 19)
    
    solution = mdl.solve()
    if solution:
        print(f"Valor ótimo (Custo): {mdl.objective_value:.2f}")
        for i in range(6):
            print(f"Ingrediente {i+1}: {x[i].solution_value:.2f}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()