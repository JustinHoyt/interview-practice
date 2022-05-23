import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.function.Function;

import org.junit.Test;

public class Fibonacci {
    static Function<Integer, Integer> fib;

    public static int fibonacci(int num) {
        Map<Integer, Integer> memo = new HashMap<>();

        fib = n -> {
            if (n <= 2) {
                return 1;
            }

            if (memo.containsKey(n)) {
                return memo.get(n);
            }

            int result = fib.apply(n-1) + fib.apply(n-2);
            memo.put(n, result);
            return result;
        };

        return fib.apply(num);
    }

    public static void main(String args[]) {
        Arrays
            .asList(args)
            .stream()
            .mapToInt(Integer::parseInt)
            .map(Fibonacci::fibonacci)
            .forEach(System.out::println);
    }

    @Test
    public void testFib() {
        assertEquals(55, fibonacci(10));
    }
}
