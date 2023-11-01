import heapq

def gbfs_maze_solver(maze):
    def heuristic(node, goal):
        # Geometria do táxi - distância de Manhattan
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    start = (0, 0)
    goal = find_goal(maze)
    came_from = {}

    open_list = []
    closed_set = set()

    heapq.heappush(open_list, (heuristic(start, goal), start))

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current, start)

        closed_set.add(current)

        for neighbor in get_neighbors(current, maze):
            if neighbor in closed_set:
                continue

            if neighbor not in {item[1] for item in open_list}:
                heapq.heappush(open_list, (heuristic(neighbor, goal), neighbor))
                came_from[neighbor] = current

    return []

def find_goal(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "B":
                return (i, j)

def get_neighbors(node, maze):
    neighbors = []
    row, col = node
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] != "1":
            neighbors.append((new_row, new_col))
    return neighbors

def reconstruct_path(came_from, current, start):
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path[::-1]

# Exemplo de uso
maze = [
    ["A", "0", "1", "1", "1", "1"],
    ["0", "0", "1", "1", "1", "1"],
    ["1", "0", "0", "0", "0", "B"],
    ["1", "1", "1", "1", "1", "1"]
]

path = gbfs_maze_solver(maze)

if path:
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if (row, col) in path:
                print("P", end=" ")
            else:
                print(maze[row][col], end=" ")
        print()
else:
    print("Caminho não encontrado.")
