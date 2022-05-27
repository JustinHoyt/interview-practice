import static org.junit.Assert.assertEquals;

import java.util.HashMap;
import java.util.Map;
import java.util.function.BiFunction;
import java.util.stream.IntStream;

import org.junit.Test;

public class LongestIncreasingPathInAMatrix {
    public static int longestIncreasingPathInAMatrix(int[][] grid) {
        var closure = new Object() {
            BiFunction<Integer, Integer, Integer> dfs;
            Map<String, Integer> memo = new HashMap<>();
        };

        closure.dfs = (i, j) -> {
            String key = i + "," + j;
            if (closure.memo.containsKey(key)) {
                return closure.memo.get(key);
            }

            int maxResult = 0;
            for (int[] point : new int[][] { {i, j+1}, {i, j-1}, {i+1, j}, {i-1, j} }) {
                int _i = point[0];
                int _j = point[1];
                if (0 <= _i && _i < grid.length &&
                    0 <= _j && _j < grid[0].length &&
                    grid[_i][_j] > grid[i][j]
                ) {
                    maxResult = Math.max((closure.dfs.apply(_i, _j) + 1), maxResult);
                }
            }
            closure.memo.put(key, maxResult);
            return maxResult;
        };

        return IntStream.range(0, grid.length).map(i ->
            IntStream.range(0, grid[0].length).map(j ->
                closure.dfs.apply(i, j) + 1
            ).max().getAsInt()
        ).max().getAsInt();

    }

    @Test
    public void testFib() {
        assertEquals(4, longestIncreasingPathInAMatrix(new int[][]{
            {3, 4, 5},
            {3, 2, 6},
            {2, 2, 1},
        }));
    }
}

