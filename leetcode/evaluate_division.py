from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []

        def make_graph(equations, values):
            graph = defaultdict(dict)
            for equation, value in zip(equations, values):
                start, end = equation
                graph[start][end] = value
                graph[end][start] = 1/value
            return graph

        graph = make_graph(equations, values)
        print(graph)

        def add_quotient(start, end, visited, sofar=1):
            if start == end and end in graph:
                result.append(sofar)
            visited.add(start)

            for node, weight in graph[start].items():
                if node not in visited:
                    add_quotient(node, end, visited, sofar * weight)

        for start, end in queries:
            size = len(result)
            add_quotient(start, end, set())
            if len(result) == size:
                result.append(-1)

        return result

print(Solution().calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]))