import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class ArraySubset {
    public static boolean arraySubset(int[] array1, int[] array2) {
        int idx1 = 0;
        int idx2 = 0;

        while (idx1 < array1.length && idx2 < array2.length) {
            if (array1[idx1] == array2[idx2]) {
                idx1 += 1;
                idx2 += 1;
            } else {
                idx1 -= idx2 - 1;
                idx2 = 0;
            }
        }

        return idx2 == array2.length;
    }

    @Test
    public void testSubsetExists() {
        assertEquals(true, arraySubset(new int[] {1,2,4,1,4,1,2,1}, new int[] {4,1,2}));
    }

    @Test
    public void testNoSubset() {
        assertEquals(false, arraySubset(new int[] {1,2,4,1,4,1,2,1}, new int[] {4,1,1}));
    }

    @Test
    public void testReuseFailedSubsetInCorrectSubset() {
        assertEquals(true, arraySubset(new int[] {1,1,1,4,1,4,1,2,1}, new int[] {1,1,4}));
    }
}
