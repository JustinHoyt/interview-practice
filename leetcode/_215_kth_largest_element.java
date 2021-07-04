package leetcode;

import java.util.Arrays;
import java.util.PriorityQueue;

public class _215_kth_largest_element {
    public static void main(String[] args) {
        int[] nums = {3,2,3,1,2,4,5,5,6};
        int k = 3;

        System.out.println(new _215_kth_largest_element().findKthLargest(nums, k));
    }

    public int findKthLargest(int[] nums, int k) {
        var minHeap = new PriorityQueue<Integer>();

        for(int num: nums) {
            minHeap.add(num);
            if(minHeap.size() > k) {
                minHeap.poll();
            }
        }

        return minHeap.poll();
    }
}
