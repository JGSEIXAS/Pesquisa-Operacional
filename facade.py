import argparse
import subprocess
import sys
import os

def run_bin_packing(time_limit):
    script_path = os.path.join("questao1_bin_packing", "solver_bin_packing.py")
    if not os.path.exists(script_path):
        print(f"Erro: O arquivo {script_path} não foi encontrado.")
        sys.exit(1)
        
    print(f"--- Executando Bin Packing com limite de {time_limit} segundos ---")
    print("Aguardando entrada dos dados (Itens, Capacidade, Pesos)...")
    print("Exemplo de formato para colar e dar Enter:")
    print("10 15")
    print("10 4 3 5 3 4 3 4 1 2\n")
    # Chama o script passando o tempo limite como argumento
    subprocess.run([sys.executable, script_path, str(time_limit)])

def run_linear_model(model_name):
    script_path = os.path.join("questao2_modelos_lineares", f"{model_name}.py")
    if not os.path.exists(script_path):
        print(f"Erro: O modelo '{model_name}' não foi encontrado em {script_path}.")
        sys.exit(1)
        
    print(f"--- Executando modelo linear: {model_name} ---")
    subprocess.run([sys.executable, script_path])

def main():
    parser = argparse.ArgumentParser(description="Facade para execução dos problemas de Pesquisa Operacional.")
    
    parser.add_argument(
        "--problem", 
        type=str, 
        required=True, 
        help="Nome do problema a ser executado (ex: bin_packing, dieta, mochila)"
    )
    
    parser.add_argument(
        "--time", 
        type=int, 
        default=5, 
        help="Tempo limite em segundos (utilizado apenas para o bin_packing)"
    )
    
    args = parser.parse_args()
    
    if args.problem == "bin_packing":
        run_bin_packing(args.time)
    else:
        run_linear_model(args.problem)

if __name__ == "__main__":
    main()