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

public class LongestIncreasingPathInAMatrix {
    public static int longestIncreasingPathInAMatrix(int[][] grid) {
        var closure = new Object() {
            BiFunction<Integer, Integer, Integer> dfs;
            ConcurrentHashMap<String, Integer> memo = new ConcurrentHashMap<>(grid.length * grid[0].length);
        };


        closure.dfs = (i, j) -> {
            BiPredicate<Integer, Integer> inBounds = (_i, _j) -> 0 <= _i && _i < grid.length && 0 <= _j && _j < grid[0].length;
            BiPredicate<Integer, Integer> largerThanPreviousPoint = (_i, _j) -> grid[_i][_j] > grid[i][j];
            return closure.memo.computeIfAbsent(i + "," + j, __ ->
                List.of(new int[][] { {i, j+1}, {i, j-1}, {i+1, j}, {i-1, j} })
                    .stream()
                    .mapToInt(neighbor ->
                        (inBounds.and(largerThanPreviousPoint).test(neighbor[0], neighbor[1]))
                            ? closure.dfs.apply(neighbor[0], neighbor[1]) + 1
                            : 0
                    )
                    .max()
                    .getAsInt()
            );
        };

        return range(0, grid.length).flatMap(i ->
            range(0, grid[0].length).map(j ->
                closure.dfs.apply(i, j) + 1
            )
        ).max().getAsInt();

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

