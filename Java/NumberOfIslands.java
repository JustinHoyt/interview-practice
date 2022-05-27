import static org.junit.Assert.assertEquals;
import static java.util.stream.IntStream.range;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.BiFunction;
import java.util.function.BiPredicate;
import java.util.function.Function;
import java.util.function.Predicate;

import org.junit.Test;

public class NumberOfIslands {
    public static int numberOfIslands(int[][] grid) {
        var closure = new Object() {
            Consumer<int[]> markIsland;
            int[][] visited = new int[grid.length][grid[0].length];
        };

        closure.markIsland = point -> {
            int i = point[0];
            int j = point[1];

            if (0 <= i && i < grid.length &&
                0 <= j && j < grid[0].length &&
                grid[i][j] == 1 &&
                closure.visited[i][j] == 0
            ) {
                closure.visited[i][j] = 1;
                for (int[] neighborPoint : new int[][] { {i+1, j}, {i-1, j}, {i, j+1}, {i, j-1}}) {
                    closure.markIsland.accept(neighborPoint);
                }
            }
        };

        BiPredicate<Integer, Integer> isLand = (i, j) -> grid[i][j] == 1;
        BiPredicate<Integer, Integer> isUnvisited = (i, j) -> closure.visited[i][j] == 0;

        return range(0, grid.length).flatMap(i ->
            range(0, grid[0].length).map(j -> {
                if (isLand.and(isUnvisited).test(i, j)) {
                    closure.markIsland.accept(new int[] {i, j});
                    return 1;
                }
                return 0;
            })
        ).sum();
    }

    @Test
    public void testFib() {
        assertEquals(2, numberOfIslands(new int[][]{
            {1, 0, 1},
            {1, 1, 1},
            {0, 0, 0},
            {0, 1, 0},
        }));
    }
}
