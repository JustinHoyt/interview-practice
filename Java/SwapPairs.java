import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.Scanner;

import org.junit.Test;

public class SwapPairs {

    public static String reversePairs(String digits) {
        char[] digitsArray = digits.toCharArray();

        for (int i = 0; i + 1 < digits.length(); i += 2) {
            char temp = digitsArray[i];
            digitsArray[i] = digitsArray[i+1];
            digitsArray[i+1] = temp;
        }

        return new String(digitsArray);
    }

    public static void main(String args[]) {
        Arrays
            .asList(args)
            .stream()
            .map(SwapPairs::reversePairs)
            .forEach(System.out::println);
    }

    @Test
    public void testEvenNumberOfLetters() {
        assertEquals(reversePairs("word"), "owdr");
    }

    @Test
    public void testOddNumberOfLetters() {
        assertEquals(reversePairs("words"), "owdrs");
    }
}
