import argparse
import time
import random
import sys

class Item:
    def __init__(self, id_item, size):
        self.id = id_item
        self.size = size

class Bin:
    def __init__(self):
        self.items = []
        self.total = 0

def best_fit_decreasing(items, capacity):
    """
    Heurística construtiva inicial (BFD).
    Ordena os itens do maior para o menor e tenta encaixá-los na caixa que deixar o menor espaço de sobra.
    """
    items.sort(key=lambda x: x.size, reverse=True)
    bins = []
    
    for item in items:
        best_idx = -1
        min_space = capacity * 2
        
        for i, b in enumerate(bins):
            space = capacity - b.total
            if item.size <= space and space < min_space:
                min_space = space
                best_idx = i
                
        if best_idx == -1:
            new_bin = Bin()
            new_bin.items.append(item)
            new_bin.total += item.size
            bins.append(new_bin)
        else:
            bins[best_idx].items.append(item)
            bins[best_idx].total += item.size
            
    return bins

def local_search(bins, capacity):
    """
    Busca Local (First Improvement).
    Tenta mover um item de uma caixa para outra. Se a caixa original ficar vazia, 
    elimina a caixa e aceita a melhoria imediatamente.
    """
    for i in range(len(bins)):
        for j in range(len(bins)):
            if i == j:
                continue
            
            k = 0
            while k < len(bins[i].items):
                item = bins[i].items[k]
                if bins[j].total + item.size <= capacity:
                    # Efetua o movimento
                    bins[j].items.append(item)
                    bins[j].total += item.size
                    
                    bins[i].total -= item.size
                    bins[i].items.pop(k)
                    
                    # Se a caixa esvaziou, reduzimos o número de bins!
                    if not bins[i].items:
                        bins.pop(i)
                        return True # First improvement aceite
                else:
                    k += 1
    return False

def iterated_local_search(bins, capacity, deadline):
    """
    Meta-heurística (ILS) que perturba a solução destruindo algumas caixas 
    e tenta reconstruí-la aplicando a busca local de seguida.
    """
    current_bins = [Bin() for _ in bins]
    for i, b in enumerate(bins):
        current_bins[i].items = list(b.items)
        current_bins[i].total = b.total

    while time.time() < deadline:
        if len(current_bins) <= 1:
            break
            
        # Perturbação: Escolhe 2 caixas para destruir
        i = random.randint(0, len(current_bins) - 1)
        j = i
        while j == i:
            j = random.randint(0, len(current_bins) - 1)
            
        removed_items = current_bins[i].items + current_bins[j].items
        random.shuffle(removed_items)
        
        # Filtra as caixas que não foram destruídas
        new_bins = [b for idx, b in enumerate(current_bins) if idx not in (i, j)]
        
        # Tenta reinserir os itens órfãos
        for item in removed_items:
            placed = False
            for b in new_bins:
                if b.total + item.size <= capacity:
                    b.items.append(item)
                    b.total += item.size
                    placed = True
                    break
            if not placed:
                new_bin = Bin()
                new_bin.items.append(item)
                new_bin.total += item.size
                new_bins.append(new_bin)
                
        # Refina a nova solução construída
        if local_search(new_bins, capacity):
            current_bins = new_bins
            
        # Avaliação: Se a perturbação + busca local encontrou algo menor, atualiza o global
        if len(new_bins) < len(bins):
            bins = list(new_bins)
            current_bins = list(new_bins)

    return bins

def main():
    parser = argparse.ArgumentParser(description="Solver Bin Packing")
    parser.add_argument("time_limit", type=int, help="Tempo limite de execução em segundos")
    args = parser.parse_args()

    # Leitura dos dados da instância via entrada padrão
    try:
        first_line = input().strip().split()
        if not first_line:
            return
        n = int(first_line[0])
        capacity = int(first_line[1])
        
        items = []
        sizes = list(map(int, input().strip().split()))
        
        for i in range(n):
            items.append(Item(id_item=i, size=sizes[i]))
            
    except Exception as e:
        print("Erro ao ler a entrada. Formato esperado:")
        print("<quantidade_itens> <capacidade>")
        print("<tamanho_1> <tamanho_2> ... <tamanho_n>")
        sys.exit(1)

    deadline = time.time() + args.time_limit

    # Geração inicial
    bins = best_fit_decreasing(items, capacity)
    random.shuffle(bins)
    
    # Execução da Meta-heurística
    best_bins = iterated_local_search(bins, capacity, deadline)

    # Saída dos resultados
    print(f"\nNúmero de bins usados: {len(best_bins)}")
    for i, b in enumerate(best_bins):
        items_str = ", ".join([f"id:{item.id}(peso:{item.size})" for item in b.items])
        print(f"Bin {i + 1} (Ocupado: {b.total}/{capacity}): {items_str}")

if __name__ == "__main__":
    main()