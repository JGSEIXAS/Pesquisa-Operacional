from docplex.mp.model import Model

def main():
    mdl = Model(name='escalonamento_enfermeiras')
         
    d = [5, 7, 6, 8, 4, 7, 5]
    a = [
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0]
    ]
    
    x = [mdl.integer_var(lb=0, name=f'x{s}') for s in range(8)]
    
    for i in range(7):
        mdl.add_constraint(mdl.sum(a[i][s] * x[s] for s in range(8)) >= d[i])
        
    mdl.minimize(mdl.sum(x[s] for s in range(8)))
    
    solution = mdl.solve()
    if solution:
        print(f"Resposta (Total Enfermeiras): {int(mdl.objective_value)}")
    else:
        print("Sem solução.")

if __name__ == "__main__":
    main()