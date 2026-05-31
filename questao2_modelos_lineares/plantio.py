from ortools.linear_solver import pywraplp

def main():
    solver = pywraplp.Solver.CreateSolver('SCIP')
    
    area_fazenda = [400, 650, 350]
    area_cultura = [660, 880, 400]
    agua_fazenda = [1800, 2200, 950]
    coef_agua = [5.5, 4.0, 3.5]
    preco = [5000, 4000, 1800]

    # Matriz de Variáveis X[fazenda][cultura]
    X = []
    for i in range(3):
        X.append([solver.IntVar(0, solver.infinity(), f'x_{i}_{j}') for j in range(3)])

    # Função Objetivo: Maximizar o lucro
    solver.Maximize(sum(preco[j] * X[i][j] for i in range(3) for j in range(3)))

    # Restrições de área por fazenda
    for i in range(3):
        solver.Add(sum(X[i][j] for j in range(3)) <= area_fazenda[i])

    # Restrições de área por cultura
    for j in range(3):
        solver.Add(sum(X[i][j] for i in range(3)) <= area_cultura[j])

    # Restrições de limite de água
    for i in range(3):
        solver.Add(sum(coef_agua[j] * X[i][j] for j in range(3)) <= agua_fazenda[i])

    # Restrição de proporção igualitária entre fazendas
    soma_fazenda = [sum(X[i][j] for j in range(3)) for i in range(3)]
    solver.Add(650.0 * soma_fazenda[0] == 400.0 * soma_fazenda[1])
    solver.Add(350.0 * soma_fazenda[0] == 400.0 * soma_fazenda[2])

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        print(f"Lucro = {solver.Objective().Value():.2f}")
        for i in range(3):
            print(f"Fazenda {i + 1}: Milho = {X[i][0].solution_value()}, Arroz = {X[i][1].solution_value()}, Feijao = {X[i][2].solution_value()}")
    else:
        print("Sem solucao")

if __name__ == "__main__":
    main()