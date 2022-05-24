import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.function.BiConsumer;
import java.util.function.BiFunction;
import java.util.function.Function;

import org.junit.Test;

public class NumberOfIslands {
    static BiConsumer<Integer, Integer> markIsland;

    public static int numberOfIslands(int[][] grid) {
        markIsland = (i, j) -> {
            if (
                0 <= i && i < grid.length &&
                0 <= j && j < grid[0].length &&
                grid[i][j] == 1
            ) {
                grid[i][j] = 0;
                for (int[] point : new int[][] { {i+1, j}, {i-1, j}, {i, j+1}, {i, j-1} }) {
                    markIsland.accept(point[0], point[1]);
                }
            }
        };

        int numIslands = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1) {
                    markIsland.accept(i, j);
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
