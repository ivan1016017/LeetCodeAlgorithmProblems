package easy_problems.from_1_to_50;

import java.util.Arrays;

public class NumbersSmallerThanCurrentNumber implements Numbers {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] arr = new int[101];

        for(int i=0; i<nums.length; i++) {
            arr[nums[i]]++;
        }

        System.out.println(Arrays.toString(arr));

        int currentCount = 0;
        for(int i=0; i<arr.length; i++) {
            int temp = arr[i];
            arr[i] = currentCount;
            if(temp > 0) {
                currentCount += temp;
            }
        }

        System.out.println(Arrays.toString(arr));

        for(int i=0; i<nums.length; i++) {
            nums[i] = arr[nums[i]];
        }

        return nums;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of a class that does not return numbers.");
    }
}
