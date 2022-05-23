import static org.junit.Assert.assertEquals;

import java.util.Arrays;

import org.junit.Test;

public class SwapPairsInt {

    public static int reversePairsIntWithClass(int num) {
        Digits digits = new Digits(num);
        Digits result = new Digits(0);

        while (digits.getLength() > 1) {
            int right = digits.pop();
            int left = digits.pop();

            result.pushLeft(left);
            result.pushLeft(right);
        }

        if (digits.getLength() == 1) {
            result.pushLeft(digits.pop());
        }

        return result.getNumber();
    }

    public static int reversePairsInt(int num) {
        int result = 0;
        int i = 0;
        while (num > 10) {
            // Get the right most digit
            int right_digit = num % 10;
            num = num / 10;

            // Get the next right most digit
            int left_digit = num % 10;
            num = num / 10;

            // Push the digit to the left most spot in the result int
            result += left_digit * Math.pow(10, i++);
            // Push the digit to the left most spot in the result int
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
            .map(SwapPairsInt::reversePairsIntWithClass)
            .forEach(System.out::println);
    }

    @Test
    public void testEvenNumberOfLettersWithClass() {
        assertEquals(2143, reversePairsIntWithClass(1234));
    }

    @Test
    public void testOddNumberOfLettersWithClass() {
        assertEquals(13254, reversePairsIntWithClass(12345));
    }

    @Test
    public void testEvenNumberOfLetters() {
        assertEquals(2143, reversePairsInt(1234));
    }

    @Test
    public void testOddNumberOfLetters() {
        assertEquals(13254, reversePairsInt(12345));
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

    public int getLength() {
        return (int) Math.ceil(Math.log10(this.num + 1));
    }

    public void pushLeft(int digit) {
        this.num += digit * Math.pow(10, this.getLength());
    }

    public int pop() {
        int digit = this.num % 10;
        this.num = this.num / 10;
        return digit;
    }
}
