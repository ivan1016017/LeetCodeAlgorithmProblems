package easy_problems.from_1_to_50;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {

    public int[] twoSum(int[] nums, int target){
        int[] result = new int[2];
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for ( int i = 0; i < nums.length; i++){

            if (map.containsKey())

            map.put(nums[i], i);
        }



        return result;

    }
}
