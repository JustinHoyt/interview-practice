import static org.junit.Assert.assertEquals;

import java.util.Arrays;

import org.junit.Test;

public class SwapPairsInt {

    public static int reversePairsIntWithClass(int num) {
        int result = 0;
        int i = 0;
        Digits digits = new Digits(num);

        while (digits.getNumber() > 10) {
            result += digits.pop() * Math.pow(10, i+1);
            result += digits.pop() * Math.pow(10, i);
            i += 2;
        }

        if (num > 0) {
            result += digits.pop() * Math.pow(10, i);
        }

        return result;
    }

    public static int reversePairsInt(int num) {
        int result = 0;
        int i = 0;
        while (num > 10) {
            int right_digit = num % 10;
            num = num / 10;

            int left_digit = num % 10;
            num = num / 10;

            result += left_digit * Math.pow(10, i++);
            result += right_digit * Math.pow(10, i++);
        }

        if (num > 0) {
            int last_digit = num % 10;
            result += last_digit * Math.pow(10, i);
        }

        return result;
    }

    public static void main(String args[]) {
        Arrays
            .asList(args)
            .stream()
            .mapToInt(Integer::parseInt)
            .map(SwapPairsInt::reversePairsInt)
            .forEach(System.out::println);
    }

    @Test
    public void testEvenNumberOfLettersWithClass() {
        assertEquals(reversePairsIntWithClass(1234), 2143);
    }

    @Test
    public void testOddNumberOfLettersWithClass() {
        assertEquals(reversePairsIntWithClass(12345), 13254);
    }

    @Test
    public void testEvenNumberOfLetters() {
        assertEquals(reversePairsInt(1234), 2143);
    }

    @Test
    public void testOddNumberOfLetters() {
        assertEquals(reversePairsInt(12345), 13254);
    }
}

class Digits {
    private int num;

    public Digits(int num) {
        this.num = num;
    }

    public int getNumber() {
        return num;
    }

    public int peak() {
        return this.num % 10;
    }

    public int pop() {
        int digit = this.num % 10;
        this.num = this.num / 10;
        return digit;
    }

}
