def bellman(graph, start, end):
    distances = {}
    for vertex in graph:
        distances[vertex] = float('inf')
    distances[start] = 0

    for _ in range(len(graph)-1):
        for vertex in graph:
            for neighbor in graph[vertex]:
                distances[neighbor] = min(distances[neighbor],
                                          distances[vertex] + graph[vertex][neighbor])
    for vertex in graph:
        for neighbor in graph[vertex]:
            if distances[vertex] + graph[vertex][neighbor] < distances[neighbor]:
                distances[neighbor] = float('-inf')
    return distances[end]


graph = {
    's': {'a': 2, 'b': 1},
    'a': {'s': 3, 'b': 4, 'c': 8},
    'b': {'s': 4, 'a': 2, 'd': 2},
    'c': {'a': 2, 'd': 7, 't': 4},
    'd': {'b': 1, 'c': 11, 't': 5},
    't': {'c': 3, 'd': 5},
}

print(bellman(graph, 's', 't'))
