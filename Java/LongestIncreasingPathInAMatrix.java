import static java.lang.Math.max;
import static java.util.stream.IntStream.range;
import static org.junit.Assert.assertEquals;

import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.function.Function;
import java.util.function.BiFunction;
import java.util.function.Predicate;
import java.util.function.BiPredicate;
import java.util.concurrent.ConcurrentHashMap;


import org.junit.Test;

record Point(int row, int col) {};

public class LongestIncreasingPathInAMatrix {

    public static int longestIncreasingPathInAMatrix(int[][] grid) {
        var closure = new Object() {
            Function<Point, Integer> search;
            ConcurrentHashMap<String, Integer> memo = new ConcurrentHashMap<>(grid.length * grid[0].length);
        };

        closure.search = current -> {
            Predicate<Point> isInBounds = next -> 0 <= next.row() && next.row() < grid.length && 0 <= next.col() && next.col() < grid[0].length;
            Predicate<Point> isLargerThanCurrentPoint = next -> grid[next.row()][next.col()] > grid[current.row()][current.col()];
            Point[] neighbors = new Point[] {
                new Point(current.row(), current.col()+1),
                new Point(current.row(), current.col()-1),
                new Point(current.row()+1, current.col()),
                new Point(current.row()-1, current.col())
            };

            return closure.memo.computeIfAbsent(current.toString(), __ ->
                List.of(neighbors)
                    .stream()
                    .mapToInt(neighbor ->
                        (isInBounds.and(isLargerThanCurrentPoint).test(neighbor))
                            ? closure.search.apply(neighbor) + 1
                            : 0
                    )
                    .max()
                    .orElse(0)
            );
        };

        return range(0, grid.length).flatMap(row ->
            range(0, grid[0].length).map(col ->
                closure.search.apply(new Point(row, col)) + 1
            )
        ).max().orElse(0);
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
