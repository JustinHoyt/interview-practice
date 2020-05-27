from math import inf

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])

        def helper(target, location, fuel, stations, idx):
            # base case
            if fuel < 0:
                return inf
            if location <= target:
                return 0

            # recursion: for each station, we want to try to go to that station and then to the end
            best_path = inf
            for j in range(idx, len(stations)):
                dist = stations[j][0] - location
                temp_path = helper(target, stations[j][0], fuel - dist + stations[j][1], stations) + 1
                best_path = min(best_path, temp_path)

            return best_path

        result = helper(target, 0, startFuel, stations)
        if result == inf:
            return -1
        return result
