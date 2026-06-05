from docplex.mp.model import Model

def main():
    mdl = Model(name='formulacao_racoes')
         
    AMGS = mdl.continuous_var(lb=0, name='AMGS')
    RE = mdl.continuous_var(lb=0, name='RE')
    
    mdl.maximize(11 * AMGS + 12 * RE)
    
    mdl.add_constraint(AMGS + 4 * RE <= 10000) 
    mdl.add_constraint(5 * AMGS + 2 * RE <= 30000) 
    
    solution = mdl.solve()
    if solution:
        print(f"Valor ótimo (Lucro): {mdl.objective_value:.2f}")
        print(f"AMGS = {AMGS.solution_value:.2f}")
        print(f"RE = {RE.solution_value:.2f}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()