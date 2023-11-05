package easy_problems.from_1_to_50;

import java.util.HashMap;

public class SumTwoNumbers {
    public int[] twoSum(int[] nums, int target) {

    HashMap<Integer,Integer> solutionHash = new HashMap<Integer,Integer>();
    for (int i = 0; i < nums.length;i++){

        if (solutionHash.containsKey(nums[i])){
            return new int[] {solutionHash.get(nums[i]),i};
        }
        else{
            solutionHash.put(target-nums[i],i);
        }
    }

    return new int[2];

    }

}

