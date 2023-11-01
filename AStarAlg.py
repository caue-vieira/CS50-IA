import heapq

def astar(graph, start, goal):
    open_list = []  # Lista de nós a serem avaliados
    closed_set = set()  # Conjunto de nós já avaliados
    came_from = {}  # Dicionário para armazenar o nó anterior para reconstruir o caminho
    g_score = {node: float('inf') for node in graph}  # G-score, o custo real do início até o nó atual
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}  # F-score, a estimativa do custo total
    f_score[start] = heuristic(start, goal)  # Usando uma função heurística para estimar o custo até o objetivo

    # Usaremos uma tupla (f_score, node) para ordenar a lista de prioridade.
    heapq.heappush(open_list, (f_score[start], start))

    while open_list:
        current = heapq.heappop(open_list)[1]
        print(current)

        if current == goal:
            return reconstruct_path(came_from, current)

        closed_set.add(current)

        for neighbor in graph[current]:
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + distance_between(current, neighbor)

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # Caminho não encontrado

def heuristic(node, goal):
    # Função heurística para estimar o custo do nó atual até o objetivo
    # Você pode personalizar essa função com base no problema específico.
    return 0

def distance_between(node1, node2):
    # Função para calcular a distância real entre dois nós
    # Você pode personalizar essa função com base no problema específico.
    return 1

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

# Exemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['I'],
    'G': ['J'],
    'H': ['K'],
    'I': [],
    'J': ['L'],
    'K': [],
    'L': []
}

start_node = 'A'
goal_node = 'L'

path = astar(graph, start_node, goal_node)
if path:
    print("Caminho encontrado:", path)
else:
    print("Caminho não encontrado.")