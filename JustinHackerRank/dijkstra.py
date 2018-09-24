def shortest_path_rec(graph, current, end, visited, distances):
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
        for vertex in graph:
            if vertex not in visited:
                unvisited[vertex] = distances[vertex]
        next_vertex = min(unvisited, key=unvisited.get)

        return shortest_path_rec(graph, next_vertex, end, visited, distances)


def shortest_path(graph, start, end):
    visited = set()
    distances = {}
    for vertex in graph:
        distances[vertex] = float('inf')
    distances[start] = 0
    visited.add(start)

    return shortest_path_rec(graph, start, end, visited, distances)


graph = {
    's': {'a': 2, 'b': 1},
    'a': {'s': 3, 'b': 4, 'c': 8},
    'b': {'s': 4, 'a': 2, 'd': 2},
    'c': {'a': 2, 'd': 7, 't': 4},
    'd': {'b': 1, 'c': 11, 't': 5},
    't': {'c': 3, 'd': 5},
}

print(shortest_path(graph, 's', 't'))



# def shortest_path_rec(graph, current, end, visited, distances, predecessors):
#     if current == end:
#         path = []
#         pred = end
#         while pred:
#             path.append(pred)
#             pred = predecessors.get(pred, None)
#         print("shortest path", path, "cost =", distances[end])
#     else:
#         for neighbor in graph[current]:
#             if neighbor not in visited:
#                 new_dist = distances[current] + graph[current][neighbor]
#                 if new_dist < distances[neighbor]:
#                     distances[neighbor] = new_dist
#                     predecessors[neighbor] = current
#         visited.add(current)
#         unvisited = {}
#         for vertex in graph:
#             if vertex not in visited:
#                 unvisited[vertex] = distances[vertex]
#         lowest_cost = min(unvisited, key=unvisited.get)
#         return shortest_path_rec(graph, lowest_cost, end, visited, distances, predecessors)

# def shortest_path(graph, start, end):
#     visited = set()
#     distances = {}
#     predecessors = {}
#     for vertex in graph:
#         distances[vertex] = float('inf')
#     distances[start] = 0
#     visited.add(start)

#     return shortest_path_rec(graph, start, end, visited, distances, predecessors)
