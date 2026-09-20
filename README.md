# Rota Mais Rápida - Dijkstra

## 📚 Estrutura de Dados 1

Projeto desenvolvido para a disciplina de Estrutura de Dados 1.

O objetivo do projeto é desenvolver um MVP de um algoritmo capaz de encontrar a rota mais rápida entre cidades utilizando a estrutura de dados Grafo e o algoritmo de menor caminho Dijkstra.

---

## 🎯 Objetivo

Desenvolver um algoritmo capaz de encontrar a rota com menor tempo estimado de deslocamento entre duas cidades.

Para isso, o mapa é representado através de um grafo ponderado, no qual:

- As cidades representam os vértices;
- As estradas representam as arestas;
- O tempo estimado de deslocamento representa o peso das arestas.

---

## 🗺️ Estrutura do Grafo

O mapa utilizado no MVP possui as seguintes cidades:

- Goiânia
- Trindade
- Inhumas
- Anápolis

As conexões entre as cidades possuem pesos que representam o tempo estimado de deslocamento em minutos.

Exemplo:

```text
Goiânia → Trindade = 20 minutos
Goiânia → Anápolis = 70 minutos
Trindade → Inhumas = 30 minutos
Inhumas → Anápolis = 35 minutos

Dessa forma, o grafo pode ser representado como:

Goiânia
   |
   | 20 min
   |
Trindade
   |
   | 30 min
   |
Inhumas
   |
   | 35 min
   |
Anápolis
🧩 Conceitos utilizados

Vértices: Os vértices representam as cidades do mapa.

Exemplo:

Goiânia
Trindade
Inhumas
Anápolis

Arestas: As arestas representam as estradas que conectam as cidades.

Pesos: Os pesos representam o tempo estimado de deslocamento entre duas cidades, medido em minutos.

🚀 Algoritmo de Dijkstra

O projeto utiliza o algoritmo de Dijkstra para encontrar o menor caminho entre uma cidade de origem e uma cidade de destino.

O algoritmo funciona mantendo a menor distância conhecida entre a cidade de origem e cada um dos outros vértices.

A cada etapa, o algoritmo seleciona a cidade ainda não visitada que possui a menor distância conhecida e verifica se existe um caminho menor para seus vizinhos.

Quando uma distância menor é encontrada, ela é atualizada.

Além das distâncias, o programa armazena a cidade anterior de cada vértice para que seja possível reconstruir a rota encontrada.

💻 Tecnologias utilizadas
Python 3
Git
GitHub

O algoritmo de Dijkstra foi implementado manualmente, sem a utilização de bibliotecas específicas de grafos.

▶️ Como executar

É necessário possuir o Python 3 instalado no computador.

No terminal, dentro da pasta do projeto, execute:

python AlgoritmoRota.py

Caso o sistema utilize python3, execute:

python3 AlgoritmoRota.py
🖥️ Funcionamento

Ao executar o programa, serão apresentadas as cidades disponíveis.

O usuário deverá informar:

Cidade de origem;
Cidade de destino.

Exemplo:

Cidades disponíveis:
- Goiânia
- Trindade
- Inhumas
- Anápolis

Digite a cidade de origem: Goiânia
Digite a cidade de destino: Anápolis

O programa então executará o algoritmo de Dijkstra e apresentará a rota encontrada e o tempo estimado.

Exemplo de resultado:

============================================================
RESULTADO
============================================================

Rota mais rápida:
Goiânia -> Anápolis

Tempo estimado: 70 minutos

Tempo aproximado: 1 hora(s) e 10 minuto(s)

============================================================
📁 Estrutura do projeto
RotaMaisRapida/
│
├── AlgoritmoRota.py
└── README.md
AlgoritmoRota.py

Contém a implementação do grafo, do algoritmo de Dijkstra e da interação com o usuário.


README.md

Documento com a descrição do projeto, conceitos utilizados e instruções de execução.

👩‍💻 Autora

Jaqueline Barbosa

Projeto desenvolvido para a disciplina de Estrutura de Dados 1.
