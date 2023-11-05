package easy_problems.from_1_to_50;

import java.util.Arrays;

public class KeepMultiplyingByTwo implements Numbers{
    public int findFinalValue(int[] nums, int original) {
        Arrays.sort(nums);

        for (int num: nums){
            if (num == original){
                original *= 2;
            }
        }

        return original;

    }

    public int findFinalValueTwo(int[] nums, int original) {
        for(int i=0;i<nums.length;i++){
            if(nums[i]==original){
                original=original*2;
                i=-1;
            }
        }
        return original;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of the class that returns numbers ");
    }
}
