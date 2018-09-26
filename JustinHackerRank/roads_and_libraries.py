def dfs(graph, road_cost, vertex, visited):
    cost = 0
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            visited.add(neighbor)
            cost += dfs(graph, road_cost, neighbor, visited) + road_cost
    return cost


def get_repair_cost(graph, road_cost, library_cost):
    if library_cost <= road_cost:
        return library_cost * len(graph)
    visited = set()
    cost = 0
    for vertex in graph:
        if vertex not in visited:
            visited.add(vertex)
            cost += dfs(graph, road_cost, vertex, visited) + library_cost
    return cost


graph = {
    7: {1},
    1: {3, 2},
    2: {1, 3},
    3: {1, 2},
    8: {6},
    6: {8, 5},
    5: {6},
}

print(get_repair_cost(graph, 2, 3))
