# Questão 2: Modelos de Programação Linear e Inteira

Este diretório contém as implementações em Python de todos os modelos de Programação Linear (PL) e Programação Linear Inteira (PLI) vistos durante a disciplina de Pesquisa Operacional. 

Os modelos foram formulados matematicamente e implementados para resolver problemas clássicos de otimização contínua e combinatória.

## Modelos Implementados

Abaixo está a lista dos ficheiros e o problema correspondente que cada um resolve:

* `clique.py`: **Problema do Clique Máximo** - Determinar o maior subgrafo completo num grafo dado.
* `cobertura.py`: **Cobertura de Conjuntos** - Otimização da localização de escolas para cobrir todos os bairros com o menor número de construções.
* `dieta.py`: **Problema da Dieta** - Minimização do custo de um composto alimentar garantindo a ingestão mínima de vitaminas.
* `enfermeiras.py`: **Escalonamento de Enfermeiras** - Minimização do número de enfermeiras contratadas para cobrir as necessidades diárias de turnos de um hospital.
* `facilidades.py`: **Localização de Facilidades** - Minimização dos custos de instalação de depósitos e de atendimento às demandas dos clientes.
* `fluxo.py`: **Fluxo Máximo** - Maximização da quantidade de gás natural enviado de um produtor para uma fábrica através de uma rede de dutos.
* `frequencia.py`: **Alocação de Frequências** - Minimização do número de frequências utilizadas por antenas para evitar interferências.
* `mochila.py`: **Problema da Mochila (Knapsack)** - Maximização do valor dos itens colocados numa mochila sem exceder a sua capacidade de peso.
* `padroes.py`: **Corte de Padrões** - Maximização do lucro na impressão e corte de padrões de folhas de metal para o fabrico de latas.
* `plantio.py`: **Otimização de Plantio** - Maximização do lucro de uma cooperativa agrícola através da distribuição ideal de culturas (milho, arroz, feijão) entre diferentes fazendas, respeitando limites de água e área.
* `racoes.py`: **Formulação de Rações** - Maximização de lucro na produção de dois tipos de ração canina, sujeita à disponibilidade de carne e cereais.
* `tintas.py`: **Mistura de Tintas** - Minimização do custo na compra de componentes para satisfazer a proporção exigida na produção de tintas de secagem rápida e normal.
* `transporte.py`: **Problema de Transporte** - Otimização de custos de transporte e distribuição.

## Como Executar

Para executar os modelos de forma organizada, recomenda-se a utilização do ficheiro de fachada (`facade.py`) localizado na raiz do repositório.

A partir do diretório raiz, executa o seguinte comando no terminal, substituindo `<nome_do_modelo>` pelo nome do ficheiro sem a extensão `.py`:

```bash
python facade.py --problem <nome_do_modelo>