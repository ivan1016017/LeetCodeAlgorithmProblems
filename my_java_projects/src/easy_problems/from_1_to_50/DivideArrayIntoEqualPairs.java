package easy_problems.from_1_to_50;

import java.util.Arrays;

public class DivideArrayIntoEqualPairs implements Numbers{
    public boolean divideArray(int[] nums) {

        int lenNums = nums.length;
        if (lenNums % 2 != 0){
            return false;
        }
        else {

            Arrays.sort(nums);

            for (int i = 0; i < Math.floor(lenNums/2);i++){
                if (nums[i*2] != nums[i*2 + 1]) return false;

            }
            return true;

        }

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an class that returns booleans instead of numbers");
    }
}
