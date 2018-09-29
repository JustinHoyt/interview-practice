import heapq

def shortest_path_rec(graph, current, end, visited, distances, unvisited):
    if current == end:
        return distances[end]
    else:
        for neighbor in graph[current]:
            if neighbor not in visited:
                new_dist = distances[current] + graph[current][neighbor]
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
        visited.add(current)
        unvisited = {}
        for vertex in range(len(graph)):
            if vertex not in visited:
                unvisited[vertex] = distances[vertex]
        next_vertex = min(unvisited, key=unvisited.get)

        return shortest_path_rec(graph, next_vertex, end, visited, distances, unvisited)


def shortest_path(graph, start, end):
    visited = set()
    distances = {}
    unvisited = set()
    for vertex in range(len(graph)):
        distances[vertex] = float('inf')
        unvisited.add(float('inf'))
    distances[start] = 0
    unvisited.pop()
    visited.add(start)

    return shortest_path_rec(graph, start, end, visited, distances, unvisited)


graph = [
    {1: 2, 2: 1},
    {0: 3, 2: 4, 3: 8},
    {0: 4, 1: 2, 4: 2},
    {1: 2, 4: 7, 5: 4},
    {2: 1, 3: 11, 5: 5},
    {3: 3, 4: 5},
]

# graph = [
#     {'a': 2, 'b': 1},
#     {'s': 3, 'b': 4, 'c': 8},
#     {'s': 4, 'a': 2, 'd': 2},
#     {'a': 2, 'd': 7, 't': 4},
#     {'b': 1, 'c': 11, 't': 5},
#     {'c': 3, 'd': 5},
# ]

print(shortest_path(graph, 0, 5))
