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

graph = {
    'a': {'b': 2.0}
}

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []

        def make_graph(equations, values):
            pass

        graph = make_graph(equations, values)

        def add_quotient(start, end, visited, sofar):
            if start == end:
                return sofar
            visited.add(start)

            for node, weight in graph[start].items():
                if node not in visited:
                    quotient = add_quotient(node, end, visited, sofar + weight)
                    if quotient != -1:
                        return quotient
            return -1

        for start, end in queries:
            add_quotient(start, end, graph, set())

        return result

