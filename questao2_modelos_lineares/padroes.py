from docplex.mp.model import Model

def main():
    mdl = Model(name='corte_padroes')
    
    x1 = mdl.integer_var(lb=0, name='x1')
    x2 = mdl.integer_var(lb=0, name='x2')
    x3 = mdl.integer_var(lb=0, name='x3')
    x4 = mdl.integer_var(lb=0, name='x4')
    y = mdl.integer_var(lb=0, name='y')
    
    mdl.maximize(
        50 * y 
        - 5 * (x1 + 2 * x2 + 4 * x4 - y) 
        - 3 * (7 * x1 + 3 * x2 + 9 * x3 + 4 * x4 - 2 * y)
    )
    
    mdl.add_constraint(x1 + x3 + x4 <= 200) 
    mdl.add_constraint(x2 <= 90)            
    mdl.add_constraint(y <= (x1 + 2 * x2 + 4 * x4)) 
    mdl.add_constraint(y <= (7 * x1 + 3 * x2 + 9 * x3 + 4 * x4) / 2) 
    
    solution = mdl.solve()
    if solution:
        print(f"Valor ótimo (Lucro): {mdl.objective_value:.2f}")
        print(f"Total de latas produzidas: {int(y.solution_value)}")
        print(f"Padrão 1: {int(x1.solution_value)}")
        print(f"Padrão 2: {int(x2.solution_value)}")
        print(f"Padrão 3: {int(x3.solution_value)}")
        print(f"Padrão 4: {int(x4.solution_value)}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()