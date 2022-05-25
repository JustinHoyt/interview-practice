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
    public static int fibonacci(int num) {
        var closure = new Object() {
            Function<Integer, Integer> fib;
            Map<Integer, Integer> memo = new HashMap<>(Map.of(
                1, 1,
                2, 1
            ));
        };

        closure.fib = n -> {
            if (closure.memo.containsKey(n)) {
                return closure.memo.get(n);
            }

            closure.memo.put(n, closure.fib.apply(n-1) + closure.fib.apply(n-2));
            return closure.memo.get(n);
        };

        return closure.fib.apply(num);
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
