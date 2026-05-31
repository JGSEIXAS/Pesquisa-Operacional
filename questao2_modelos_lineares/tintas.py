from ortools.linear_solver import pywraplp

def main():
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Dados
    V = [1000, 250] # SR, SN
    sec_min = [0.25 * V[0], 0.20 * V[1]]
    cor_min = [0.50 * V[0], 0.50 * V[1]]
    comp_sec = [0.30, 0.60, 1.00, 0.00]
    comp_cor = [0.70, 0.40, 0.00, 1.00]
    custo = [1.50, 1.00, 4.00, 6.00]
    nomes = ["SolA", "SolB", "SEC", "COR"]

    # Variáveis Inteiras x[p][i]
    x = []
    for p in range(2):
        x.append([solver.IntVar(0, solver.infinity(), f'x_{p}_{i}') for i in range(4)])

    # Restrição: Volume total por produto
    for p in range(2):
        solver.Add(sum(x[p][i] for i in range(4)) == V[p])

    # Restrição: Mínimo de secante e corante
    for p in range(2):
        solver.Add(sum(comp_sec[i] * x[p][i] for i in range(4)) >= sec_min[p])
        solver.Add(sum(comp_cor[i] * x[p][i] for i in range(4)) >= cor_min[p])

    # Função Objetivo: Minimizar custo total
    solver.Minimize(sum(custo[i] * x[p][i] for p in range(2) for i in range(4)))

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        for p in range(2):
            prod = "SR" if p == 0 else "SN"
            print(f"{prod}:")
            for i in range(4):
                print(f"  {nomes[i]} = {int(x[p][i].solution_value())} L")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()