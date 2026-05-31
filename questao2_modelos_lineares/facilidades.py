from ortools.linear_solver import pywraplp

def main():
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    # Dados de Exemplo (Instância pequena para teste)
    n = 3 # Número de potenciais depósitos
    m = 4 # Número de clientes
    f = [100, 150, 120] # Custo de instalação de cada depósito
    c = [               # Custo de atendimento (depósito i -> cliente j)
        [10, 20, 30, 40],
        [20, 15, 25, 30],
        [30, 25, 20, 15]
    ]

    # Variáveis
    # y[i] = 1 se o depósito i for instalado
    y = [solver.BoolVar(f'y{i}') for i in range(n)]
    # X[i][j] = 1 se o depósito i atende o cliente j
    X = [[solver.BoolVar(f'x_{i}_{j}') for j in range(m)] for i in range(n)]

    # Função Objetivo: Minimizar instalação + atendimento
    custo_instalacao = sum(y[i] * f[i] for i in range(n))
    custo_atendimento = sum(X[i][j] * c[i][j] for i in range(n) for j in range(m))
    solver.Minimize(custo_instalacao + custo_atendimento)

    # Restrições
    for j in range(m):
        # 1. Cada cliente deve ser atendido por exatamente 1 depósito
        solver.Add(sum(X[i][j] for i in range(n)) == 1)
        for i in range(n):
            # 2. Só pode atender o cliente se o depósito estiver instalado
            solver.Add(X[i][j] <= y[i])

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Custo ótimo: {solver.Objective().Value()}")
        for i in range(n):
            if y[i].solution_value() > 0.5:
                atendidos = [j+1 for j in range(m) if X[i][j].solution_value() > 0.5]
                print(f"Depósito {i+1} instalado. Atende clientes: {atendidos}")
    else:
        print("Sem solução viável.")

if __name__ == "__main__":
    main()