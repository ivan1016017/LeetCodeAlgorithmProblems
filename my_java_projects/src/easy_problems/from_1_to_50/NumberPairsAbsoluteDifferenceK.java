package easy_problems.from_1_to_50;

import java.util.HashMap;

public class NumberPairsAbsoluteDifferenceK implements Numbers{
    public int countKDifference(int[] nums, int k) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();

        int solution = 0;

        for (int i = 0; i < nums.length; i++){
            if(map.containsKey(nums[i]-k)){
                solution += map.get(nums[i] -k);
            }
            if (map.containsKey(nums[i]+k)){
                solution += map.get(nums[i]+k);
            }
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
        }
        return solution;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This class does return numbers");
    }
}
