package easy_problems.from_1_to_50;

public class RunningSum implements Numbers{
    public int[] runningSum(int[] nums) {

        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }

        return nums;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that returns arrays instead of numbers.");
    }
}