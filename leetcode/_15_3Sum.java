package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class _15_3Sum {
    public static void main(String[] args) {
//        int[] nums = {-1,0,1,2,-1,-3};
        int[] nums = {1,1,-2};

        new _15_3Sum().threeSum(nums).forEach(System.out::println);
    }

    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        var occurrencesMap = new HashMap<Integer, List<Integer>>();
        System.out.println(Arrays.toString(nums));
        for(int i = 0; i < nums.length; i++) {
            var indexes = occurrencesMap.getOrDefault(nums[i], new ArrayList<>());
            indexes.add(i);
            occurrencesMap.put(nums[i], indexes);
        }
        occurrencesMap.forEach((k, v) -> System.out.println("Key: " + k + "\nValue: " + v));
        for(int i = 0; i < nums.length; i++) {
            result.addAll(twoSum(nums, -nums[i], i));
        }
        return result;
    }

    public List<List<Integer>> twoSum(int[] nums, int target, int ignoreIdx) {
        List<List<Integer>> result = new ArrayList<>();

        int i = 0;
        int j = nums.length - 1;
        while(i < j) {
            if(i == ignoreIdx) {
                i++;
            } else if(j == ignoreIdx) {
                j--;
            } else {
                int sum = nums[i] + nums[j];
                if (sum == target) {
                    result.add(Arrays.asList(nums[i], nums[j], -target));
                    i++;
                    j--;
                } else if (sum > 0)
                    j--;
                else
                    i++;
            }
        }
        return result;
    }
}
