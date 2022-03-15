from heapq import heappop, heappush
from typing import List, Tuple

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) < 2 or len(heightMap[0]) < 2:
            return 0

        heap: List[Tuple[int, Tuple[int, int]]] = []
        visited = set()
        rain_water = 0

        # Fill heap with all items on the edges
        for r in [0, len(heightMap) - 1]:
            for c in range(len(heightMap[0])):
                heappush(heap, (heightMap[r][c], (r, c)))
                visited.add((r, c))

        for c in [0, len(heightMap[0]) - 1]:
            for r in range(len(heightMap)):
                heappush(heap, (heightMap[r][c], (r, c)))
                visited.add((r, c))

        # Capture water as we go through the heightMap in order of lowest height
        while heap:
            height, (r, c) = heappop(heap)
            visited.add((r, c))
            for _r, _c in [[r, c+1], [r, c-1], [r+1, c], [r-1, c]]:
                if (0 <= _r < len(heightMap)
                        and 0 <= _c < len(heightMap[0])
                        and (_r, _c) not in visited):
                    _height = heightMap[_r][_c]
                    rain_water += max(height - _height, 0)
                    new_height = max(height, _height)
                    heightMap[_r][_c] += new_height
                    heappush(heap, (new_height, (_r, _c)))

        return rain_water


def test_happy_path():
    assert Solution().trapRainWater([
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
    ]) == 4

def test_1D_array():
    assert Solution().trapRainWater([
        [2,3,3,2,3,1]
    ]) == 0

    assert Solution().trapRainWater([
        [2],
        [3],
        [3],
        [2],
        [3],
        [1]
    ]) == 0

if __name__ == "__main__":
    test_happy_path()

