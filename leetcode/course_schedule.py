def dfs(graph, curr_vertex, visited):
    if curr_vertex not in graph:
        return True
    for edge in graph[curr_vertex]:
        if edge in visited:
            return False
        else:
            visited.add(edge)
            return dfs(graph, edge, visited)
    return True


def can_finish_courses(graph):
    for vertex in graph:
        visited = set()
        if not dfs(graph, vertex, visited):
            return False
    return True


cycle_classes = {
    1: {0, 4},
    0: {2},
    2: {3, 1},
}
print(can_finish_courses(cycle_classes))

non_cycle_classes = {
    1: {0, 4},
    0: {2},
    2: {3},
}
print(can_finish_courses(non_cycle_classes))
