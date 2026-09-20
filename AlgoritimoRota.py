# ============================================================
# PROJETO: Rota Mais Rápida entre Goiânia e Anápolis
# Algoritmo: Dijkstra
# Linguagem: Python
# ============================================================


# ------------------------------------------------------------
# 1. REPRESENTAÇÃO DO GRAFO
# ------------------------------------------------------------
# O grafo representa o nosso mapa.
# Cada cidade é um VÉRTICE.
# Cada ligação entre duas cidades é uma ARESTA.
# O valor da aresta representa o PESO.
# Neste projeto, o peso representa o tempo estimado
# de deslocamento em minutos.
# ------------------------------------------------------------

grafo = {

    "Goiânia": {
        "Trindade": 20,
        "Anápolis": 70
    },

    "Trindade": {
        "Goiânia": 20,
        "Inhumas": 30
    },

    "Inhumas": {
        "Trindade": 30,
        "Anápolis": 35
    },

    "Anápolis": {
        "Goiânia": 70,
        "Inhumas": 35
    }
}


# ------------------------------------------------------------
# 2. ALGORITMO DE DIJKSTRA
# ------------------------------------------------------------
# O algoritmo de Dijkstra encontra o menor caminho entre
# um ponto de origem e os demais vértices de um grafo
# quando os pesos das arestas não são negativos.
#
# Neste projeto, os pesos representam minutos de viagem,
# portanto todos os pesos são positivos.
# ------------------------------------------------------------

def dijkstra(grafo, origem, destino):

    # --------------------------------------------------------
    # Dicionário que armazenará a menor distância conhecida
    # entre a origem e cada cidade.
    # --------------------------------------------------------

    distancias = {}

    for cidade in grafo:
        distancias[cidade] = float("inf")

    # A distância da origem para ela mesma é zero.
    distancias[origem] = 0


    # --------------------------------------------------------
    # Dicionário utilizado para armazenar o caminho.
    #
    # Exemplo:
    #
    # anterior["Anápolis"] = "Inhumas"
    #
    # Isso significa que, para chegar a Anápolis pelo menor
    # caminho encontrado, devemos passar anteriormente por
    # Inhumas.
    # --------------------------------------------------------

    anteriores = {}

    for cidade in grafo:
        anteriores[cidade] = None


    # --------------------------------------------------------
    # Conjunto de cidades que já foram processadas.
    # --------------------------------------------------------

    visitados = set()


    # --------------------------------------------------------
    # Loop principal do algoritmo.
    # --------------------------------------------------------

    while len(visitados) < len(grafo):

        cidade_atual = None

        # ----------------------------------------------------
        # Procuramos a cidade não visitada com a menor
        # distância conhecida.
        # ----------------------------------------------------

        menor_distancia = float("inf")

        for cidade in grafo:

            if cidade not in visitados:

                if distancias[cidade] < menor_distancia:

                    menor_distancia = distancias[cidade]
                    cidade_atual = cidade


        # ----------------------------------------------------
        # Se não encontramos uma cidade, significa que não
        # existe caminho disponível.
        # ----------------------------------------------------

        if cidade_atual is None:
            break


        # ----------------------------------------------------
        # Marcamos a cidade atual como visitada.
        # ----------------------------------------------------

        visitados.add(cidade_atual)


        # ----------------------------------------------------
        # Se chegamos ao destino, podemos parar.
        # ----------------------------------------------------

        if cidade_atual == destino:
            break


        # ----------------------------------------------------
        # Analisamos todas as cidades vizinhas da cidade atual.
        # ----------------------------------------------------

        for vizinho, peso in grafo[cidade_atual].items():

            # Calculamos uma nova distância.
            nova_distancia = (
                distancias[cidade_atual] + peso
            )


            # ------------------------------------------------
            # Se o novo caminho for menor que o caminho
            # conhecido anteriormente, atualizamos.
            # ------------------------------------------------

            if nova_distancia < distancias[vizinho]:

                distancias[vizinho] = nova_distancia

                anteriores[vizinho] = cidade_atual


    # --------------------------------------------------------
    # 3. RECONSTRUÇÃO DO CAMINHO
    # --------------------------------------------------------
    # Agora que o algoritmo encontrou a menor distância,
    # precisamos descobrir quais cidades formam o caminho.
    # --------------------------------------------------------

    caminho = []

    cidade_atual = destino

    while cidade_atual is not None:

        caminho.append(cidade_atual)

        cidade_atual = anteriores[cidade_atual]


    # Como construímos o caminho do destino para a origem,
    # precisamos inverter a lista.
    caminho.reverse()


    # --------------------------------------------------------
    # Verificamos se realmente existe um caminho.
    # --------------------------------------------------------

    if distancias[destino] == float("inf"):

        return None, float("inf")


    return caminho, distancias[destino]


# ------------------------------------------------------------
# 4. PROGRAMA PRINCIPAL
# ------------------------------------------------------------

print("=" * 60)
print("        SISTEMA DE ROTA MAIS RÁPIDA")
print("=" * 60)

print("\nCidades disponíveis:")

for cidade in grafo:
    print("-", cidade)


# ------------------------------------------------------------
# Solicita ao usuário a cidade de origem.
# ------------------------------------------------------------

origem = input("\nDigite a cidade de origem: ")


# ------------------------------------------------------------
# Solicita ao usuário a cidade de destino.
# ------------------------------------------------------------

destino = input("Digite a cidade de destino: ")


# ------------------------------------------------------------
# Verifica se as cidades informadas existem no grafo.
# ------------------------------------------------------------

if origem not in grafo or destino not in grafo:

    print("\nErro: uma das cidades informadas não existe no mapa.")


else:

    # --------------------------------------------------------
    # Executa o algoritmo de Dijkstra.
    # --------------------------------------------------------

    caminho, tempo = dijkstra(grafo, origem, destino)


    # --------------------------------------------------------
    # Verifica se existe um caminho.
    # --------------------------------------------------------

    if caminho is None:

        print("\nNão existe uma rota entre essas cidades.")

    else:

        print("\n" + "=" * 60)
        print("RESULTADO")
        print("=" * 60)

        print("\nRota mais rápida:")

        # Mostra as cidades separadas por uma seta.
        print(" -> ".join(caminho))

        print(f"\nTempo estimado: {tempo} minutos")

        # Converte minutos para horas e minutos.
        horas = tempo // 60
        minutos = tempo % 60

        if horas > 0:

            print(
                f"Tempo aproximado: "
                f"{horas} hora(s) e {minutos} minuto(s)"
            )

        else:

            print(
                f"Tempo aproximado: "
                f"{minutos} minuto(s)"
            )

        print("=" * 60)