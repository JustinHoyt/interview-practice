def find_quotient(graph, start, end, visited):
    if start == end:
        return 1
    visited.add(start)
    for edge, weight in graph.items():
        if edge[0] == start and edge[1] not in visited:
            temp = find_quotient(graph, edge[1], end, visited)
            if temp != -1:
                return temp * weight
    return -1


graph = {
    ('a','b'): 2.0,
    ('b','a'): 1/2.0,
    ('b','c'): 3.0,
    ('c','b'): 1/3.0,
}
print(find_quotient(graph, 'a', 'c', set()))
