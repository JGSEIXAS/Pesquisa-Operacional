from docplex.mp.model import Model

def main():
    mdl = Model(name='otimizacao_plantio')
         
    area_fazenda = [400, 650, 350]
    area_cultura = [660, 880, 400]
    agua_fazenda = [1800, 2200, 950]
    coef_agua = [5.5, 4.0, 3.5]
    preco = [5000, 4000, 1800]
    
    X = []
    for i in range(3):
        X.append([mdl.integer_var(lb=0, name=f'x_{i}_{j}') for j in range(3)])
        
    mdl.maximize(mdl.sum(preco[j] * X[i][j] for i in range(3) for j in range(3)))
    
    for i in range(3):
        mdl.add_constraint(mdl.sum(X[i][j] for j in range(3)) <= area_fazenda[i])
        
    for j in range(3):
        mdl.add_constraint(mdl.sum(X[i][j] for i in range(3)) <= area_cultura[j])
        
    for i in range(3):
        mdl.add_constraint(mdl.sum(coef_agua[j] * X[i][j] for j in range(3)) <= agua_fazenda[i])
        
    soma_fazenda = [mdl.sum(X[i][j] for j in range(3)) for i in range(3)]
    mdl.add_constraint(650.0 * soma_fazenda[0] == 400.0 * soma_fazenda[1])
    mdl.add_constraint(350.0 * soma_fazenda[0] == 400.0 * soma_fazenda[2])
    
    solution = mdl.solve()
    if solution:
        print(f"Lucro = {mdl.objective_value:.2f}")
        for i in range(3):
            print(f"Fazenda {i + 1}: Milho = {X[i][0].solution_value}, Arroz = {X[i][1].solution_value}, Feijao = {X[i][2].solution_value}")
    else:
        print("Sem solucao")

if __name__ == "__main__":
    main()