# Pesquisa Operacional - Otimização Combinatória e Contínua

Repositório destinado à resolução da lista de exercícios práticos da disciplina de Pesquisa Operacional do Instituto de Computação (IC) da Universidade Federal de Alagoas (UFAL).

**Autor:** João Gabriel Seixas Santos  
**Professores:** Bruno Nogueira e Rian Pinheiro

---

## Estrutura do Projeto
O projeto está organizado para isolar a meta-heurística dos modelos matemáticos, centralizando a execução através de um único ficheiro de entrada (`facade.py`).

```text
pesquisa-operacional-ufal/
├── README.md
├── .gitignore
├── facade.py
├── questao1_bin_packing/
│   └── solver_bin_packing.py
└── questao2_modelos_lineares/
    ├── clique.py
    ├── cobertura.py
    ├── dieta.py
    ├── enfermeiras.py
    ├── facilidades.py
    ├── fluxo.py
    ├── frequencia.py
    ├── mochila.py
    ├── padroes.py
    ├── plantio.py
    ├── racoes.py
    ├── tintas.py
    └── transporte.py