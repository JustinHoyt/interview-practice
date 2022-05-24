import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.BiFunction;
import java.util.function.Function;

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

        int numIslands = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1 && closure.visited[i][j] == 0) {
                    closure.markIsland.accept(new int[] {i, j});
                    numIslands++;
                }
            }
        }
        return numIslands;
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
