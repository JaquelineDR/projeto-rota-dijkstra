# 🗺️ Rota Mais Rápida — Algoritmo de Dijkstra

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Data Structures](https://img.shields.io/badge/Estrutura%20de%20Dados-Grafos-orange?style=for-the-badge)
![License](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)

MVP de um algoritmo de roteamento desenvolvido para a disciplina de **Estrutura de Dados 1**. O sistema encontra o caminho mais rápido entre cidades goianas utilizando a estrutura de dados **Grafo** e o algoritmo de **Dijkstra**.

---

## 🎯 Objetivo

Calcular a rota com o menor tempo estimado de deslocamento entre duas cidades escolhidas pelo usuário.

O mapa rodoviário é modelado através de um **Grafo Ponderado e Não-Direcionado**, onde:
- **Vértices (Nós):** Representam as cidades.
- **Arestas (Conexões):** Representam as rodovias/estradas.
- **Pesos:** Representam o tempo estimado de deslocamento em minutos.

---

## 🗺️ Estrutura do Grafo

O grafo engloba conexões rodoviárias no estado de Goiás entre as cidades de **Goiânia, Trindade, Inhumas e Anápolis**.

### Conexões e Pesos (Minutos)

- **Goiânia ↔ Trindade:** 20 min
- **Goiânia ↔ Anápolis:** 70 min
- **Trindade ↔ Inhumas:** 30 min
- **Inhumas ↔ Anápolis:** 35 min

### Visualização do Grafo

```text
       (20 min)               (30 min)               (35 min)
Goiânia ───────► Trindade ─────────────► Inhumas ─────────────► Anápolis
   │                                                               ▲
   └───────────────────────────────────────────────────────────────┘
                               (70 min)
```
## 🧩 Conceitos de Teoria dos Grafos AplicadosVértices ($V$): Cidades cadastradas no sistema (Goiânia, Trindade, Inhumas, Anápolis). 

Arestas ($E$): Ligação direta entre duas cidades.Pesos ($W$): Custo de travessia da aresta, medido em minutos de viagem.🚀 Algoritmo de DijkstraO algoritmo de Dijkstra é utilizado para encontrar o caminho de menor custo a partir de um nó de origem até todos os outros vértices do grafo.

Funcionamento no Projeto: Inicializa as distâncias de todas as cidades como infinitas, exceto a cidade de origem (que recebe distância 0). Mantém o controle das cidades visitadas e não visitadas. A cada passo, escolhe a cidade não visitada com a menor distância conhecida. Atualiza a distância estimada para os vizinhos caso um caminho mais curto seja encontrado (Relaxamento de Arestas). Armazena o vértice predecessor de cada cidade para reconstituir e exibir a rota completa ao final.

💡 Nota de Implementação: O algoritmo e a estrutura do grafo foram implementados inteiramente do zero em Python pura, sem o uso de bibliotecas de grafos externas (como NetworkX).

💻 Tecnologias UtilizadasLinguagem: Python 3Controle de Versão: Git & GitHub

📁 Estrutura do RepositórioPlaintextRotaMaisRapida/

```
│
├── AlgoritmoRota.py    # Código-fonte principal (Grafo, Dijkstra e CLI)
└── README.md           # Documentação do projeto
```

▶️ Como ExecutarPré-requisitosTer o Python 3.x instalado em seu sistema.
Passo a PassoClone o repositório:Bashgit clone [https://github.com/jaquecarvalho12/RotaMaisRapida.git](https://github.com/jaquecarvalho12/RotaMaisRapida.git)
cd RotaMaisRapida
Execute o script:Bashpython AlgoritmoRota.py
(Caso utilize Linux/macOS, use python3 AlgoritmoRota.py)
🖥️ Exemplo de Uso
Ao iniciar o programa, informe as cidades desejadas exatamente conforme a lista exibida:
```
Cidades disponíveis:
- Goiânia
- Trindade
- Inhumas
- Anápolis

Digite a cidade de origem: Goiânia
Digite a cidade de destino: Anápolis

============================================================
RESULTADO
============================================================

Rota mais rápida:
Goiânia -> Anápolis

Tempo estimado: 70 minutos
Tempo aproximado: 1 hora(s) e 10 minuto(s)

============================================================
```

👩‍💻 Autora: Jaqueline Barbosa Carvalho

GitHub: JaquelineDR

LinkedIn: www.linkedin.com/in/jaquecarvalho12

Projeto desenvolvido para a disciplina de Estrutura de Dados 1 — Instituto Federal de Goiás (IFG).
