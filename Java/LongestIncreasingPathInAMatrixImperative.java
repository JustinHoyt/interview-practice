import static java.lang.Math.max;
import static java.util.stream.IntStream.range;
import static org.junit.Assert.assertEquals;

import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.function.BiFunction;
import java.util.function.BiPredicate;
import java.util.concurrent.ConcurrentHashMap;


import org.junit.Test;

public class LongestIncreasingPathInAMatrixImperative {
    private static Map<String, Integer> memo = new HashMap<>();

    public static int dfs(int[][] grid, int i, int j) {
        String key = i + "," + j;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }

        int maxResult = 0;
        for (int[] point : new int[][] { {i, j+1}, {i, j-1}, {i+1, j}, {i-1, j} }) {
            int _i = point[0];
            int _j = point[1];
            if (0 <= _i && _i < grid.length &&
                0 <= _j && _j < grid[0].length &&
                grid[_i][_j] > grid[i][j]
            ) {
                maxResult = max((dfs(grid, _i, _j) + 1), maxResult);
            }
        }
        memo.put(key, maxResult);
        return maxResult;
    }

    public static int longestIncreasingPathInAMatrix(int[][] grid) {
        int result = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                result = max(dfs(grid, i, j) + 1, result);
            }
        }
        return result;
    }

    @Test
    public void testLongestIncreasingPath() {
        assertEquals(4, longestIncreasingPathInAMatrix(new int[][]{
            {3, 4, 5},
            {3, 2, 6},
            {2, 2, 1},
        }));
    }
}

