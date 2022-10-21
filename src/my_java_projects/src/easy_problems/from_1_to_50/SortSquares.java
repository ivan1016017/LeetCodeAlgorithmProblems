package easy_problems.from_1_to_50;

import java.util.Arrays;

public class SortSquares implements Numbers{
    public int[] sortedSquares(int[] nums) {

        for (int i = 0; i < nums.length; i++){
            nums[i] = nums[i]*nums[i];
        }

        Arrays.sort(nums);

        return nums;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that does not return numbers");
    }
}
