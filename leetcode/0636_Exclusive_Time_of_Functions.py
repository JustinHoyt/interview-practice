from typing import *

class Solution(object):
    '''docstring'''
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        '''docstring'''
        time_matrix = [[0 for x in range(100)] for y in range(n)]

        for log in logs:
            id, start_or_end, idx = log.split(":")




sol = Solution()
print(sol.exclusiveTime(n=2, logs=["0:start:0","1:start:2","1:end:5","0:end:6"]))
