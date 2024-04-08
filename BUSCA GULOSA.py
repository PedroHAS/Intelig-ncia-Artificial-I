def busca_gulosa(grafo, cidade_atual, cidades_visitadas, atrações):

    cidades_visitadas.append(cidade_atual)
    

    if len(cidades_visitadas) == len(grafo):
        return cidades_visitadas
    

    conexoes = grafo[cidade_atual]
    

    conexoes_ordenadas = sorted(conexoes.items(), key=lambda x: atrações.get(x[0], 0), reverse=True)

    for prox_cidade, _ in conexoes_ordenadas:
        if prox_cidade not in cidades_visitadas:

            return busca_gulosa(grafo, prox_cidade, cidades_visitadas, atrações)
    

    return cidades_visitadas


grafo_entregas = {
    "A": {'B': 10, 'C': 20, 'D': 15},
    "B": {'A': 10, 'C': 25, 'E': 30},
    "C": {'A': 20, 'B': 25, 'D': 35, 'E': 40},
    "D": {'A': 15, 'C': 35 , 'E': 45},
    "E": {'B': 30, 'C': 40, 'D': 45},
}


atracoes = {
    "B": "CLUBE AQUÁTICO",
    "C": "SHOW DA TURMA DA MÔNICA",
    "E": "APRESENTAÇÃO DE UM CORAL"
}


cidade_inicial = "A"


caminho_percurso = busca_gulosa(grafo_entregas, cidade_inicial, [], atracoes)


print("Caminho percorrido:")
for cidade in caminho_percurso:
    print(cidade, "-", atracoes.get(cidade, "Sem atração turística"))
