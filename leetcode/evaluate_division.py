from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        graph = defaultdict(dict)

        for (start, end), value in zip(equations, values):
            graph[start][end] = value
            graph[end][start] = 1/value

        def add_quotient(start, end, visited, sofar=1):
            if start == end and end in graph:
                return 1
            visited.add(start)

            for node, weight in graph[start].items():
                if node not in visited:
                    path_cost = add_quotient(node, end, visited, sofar * weight)
                    if path_cost != -1:
                        return path_cost * weight
            return -1

        for start, end in queries:
            result.append(add_quotient(start, end, set()))

        return result

print(Solution().calcEquation([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]))