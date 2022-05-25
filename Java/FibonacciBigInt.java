import static org.junit.Assert.assertEquals;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.function.Function;

import org.junit.Test;

public class Fibonacci {
    public static BigInteger fibonacci(int num) {
        var one = BigInteger.ONE;
        var two = BigInteger.TWO;

        var closure = new Object() {
            Function<BigInteger, BigInteger> fib;
            Map<BigInteger, BigInteger> memo = new HashMap<>(Map.of(
                one, one,
                two, one
            ));
        };

        closure.fib = (BigInteger n) -> {
            if (closure.memo.containsKey(n)) {
                return closure.memo.get(n);
            }

            closure.memo.put(n, closure.fib.apply(n.subtract(one)).add(closure.fib.apply(n.subtract(two))));
            return closure.memo.get(n);
        };

        return closure.fib.apply(BigInteger.valueOf(num));
    }

    public static void main(String args[]) {
        Arrays
            .asList(args)
            .stream()
            .mapToInt(Integer::parseInt)
            .mapToObj(Fibonacci::fibonacci)
            .forEach(System.out::println);
    }

    @Test
    public void testFib() {
        assertEquals(BigInteger.valueOf(55), fibonacci(10));
    }

    @Test
    public void testBigNumber() {
        assertEquals(
            new BigInteger(
            "4346655768693745643568852767504062580256466051737178040248172908" +
            "9536555417949051890403879840079255169295922593080322634775209689" +
            "6232398733224711616429964409065331879382989696499285160037044761" +
            "37795166849228875"
        ),
            fibonacci(1000)
        );
    }
}
