# Questão 1: Meta-heurística para o Bin Packing

Este diretório contém a solução para o problema clássico de Bin Packing (BP), utilizando uma meta-heurística baseada em busca local (*Iterated Local Search*).

## Respostas aos Requisitos da Implementação

** (a) Representação da Solução:**
A solução foi modelada utilizando Orientação a Objetos. Criou-se uma classe `Bin` (recipiente) que armazena uma lista de objetos `Item` e mantém um atributo com a soma total do tamanho ocupado. A solução completa é manipulada como uma lista de instâncias de `Bin` (`[Bin, Bin, ...]`). Quando um item é movido, ele é retirado da lista de uma instância e inserido em outra, atualizando os respectivos totais.

** (b) Função de Avaliação:**
O custo de uma solução é calculado puramente pela quantidade de recipientes abertos. O objetivo da função de avaliação é minimizar o tamanho da lista de `Bins` (ou seja, `len(bins)`). Soluções com um tamanho de lista menor são consideradas melhores.

** (c) Estratégia de Busca Local:**
Foi definida uma estrutura de vizinhança baseada na troca de itens entre dois recipientes. O algoritmo implementa uma busca do tipo **First Improvement**. Ele itera sobre todas as caixas tentando mover itens para caixas diferentes que possuam capacidade disponível. Assim que um movimento resulta no esvaziamento completo de uma caixa (reduzindo o custo geral em 1), o movimento é aceito imediatamente, a caixa vazia é eliminada, e a busca retorna sucesso.

** (d) Critério de Parada:**
O algoritmo não utiliza número de iterações fixo. Ele recebe um limite de tempo em segundos diretamente via linha de comando no momento da execução. O laço principal verifica a cada iteração o tempo decorrido e encerra a execução assim que o prazo (`deadline`) é atingido.

## Como Executar

O script recebe o tempo limite (em segundos) via argumento. Os dados da instância (quantidade de itens, capacidade e os pesos) devem ser fornecidos pela entrada padrão.

```bash
python solver_bin_packing.py <tempo_limite>