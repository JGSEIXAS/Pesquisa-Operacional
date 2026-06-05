from docplex.mp.model import Model

def main():
    mdl = Model(name='mistura_tintas')
          
    V = [1000, 250] 
    sec_min = [0.25 * V[0], 0.20 * V[1]]
    cor_min = [0.50 * V[0], 0.50 * V[1]]
    comp_sec = [0.30, 0.60, 1.00, 0.00]
    comp_cor = [0.70, 0.40, 0.00, 1.00]
    custo = [1.50, 1.00, 4.00, 6.00]
    nomes = ["SolA", "SolB", "SEC", "COR"]
    
    x = []
    for p in range(2):
        x.append([mdl.integer_var(lb=0, name=f'x_{p}_{i}') for i in range(4)])
        
    for p in range(2):
        mdl.add_constraint(mdl.sum(x[p][i] for i in range(4)) == V[p])
        
    for p in range(2):
        mdl.add_constraint(mdl.sum(comp_sec[i] * x[p][i] for i in range(4)) >= sec_min[p])
        mdl.add_constraint(mdl.sum(comp_cor[i] * x[p][i] for i in range(4)) >= cor_min[p])
        
    mdl.minimize(mdl.sum(custo[i] * x[p][i] for p in range(2) for i in range(4)))
    
    solution = mdl.solve()
    if solution:
        # Acessa o valor da função objetivo diretamente do modelo ou do objeto solution
        for p in range(2):
            prod = "SR" if p == 0 else "SN"
            print(f"{prod}:")
            for i in range(4):
                print(f"  {nomes[i]} = {int(x[p][i].solution_value)} L")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()