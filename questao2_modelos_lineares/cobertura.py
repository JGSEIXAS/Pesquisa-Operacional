from docplex.mp.model import Model

def main():
    mdl = Model(name='cobertura_conjuntos')
         
    n = 5
    adj = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 4],
        3: [1],
        4: [2]
    }
    
    x = [mdl.binary_var(name=f'x{i}') for i in range(n)]
    
    mdl.minimize(mdl.sum(x[i] for i in range(n)))
    
    for u in range(n):
        vizinhanca = [x[u]] + [x[v] for v in adj[u]]
        mdl.add_constraint(mdl.sum(vizinhanca) >= 1)
        
    solution = mdl.solve()
    if solution:
        print(f"Número mínimo de escolas: {int(mdl.objective_value)}")
        escolas = [i+1 for i in range(n) if x[i].solution_value > 0.5]
        print(f"Construir nos bairros: {escolas}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()