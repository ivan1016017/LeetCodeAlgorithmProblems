package easy_problems.from_1_to_50;

public class MaximumSubarray implements Numbers{

    public MaximumSubarray() {
        System.out.println("An instance of the class was created");
    }

    public int maxSubArray(int[] nums) {
        int n = nums.length, localMax = 0, globalMax = (int)-Math.pow(10,10);

        for (int i = 0; i < n; i++){
            localMax = Math.max(nums[i],nums[i]+ localMax);
            if (localMax > globalMax){
                globalMax = localMax;
            }
        }

        return globalMax;

    }


    @Override
    public void returnNumbers() {
        System.out.println("The class MaximumSubarray returns numbers");
    }
}
