package easy_problems.from_1_to_50;

import java.util.Collections;

public class GreatestCommonDivisor implements Numbers{
    public int findGCD(int[] nums) {

        int min_number = 10000;
        int max_number = -10000;
        int solution = -1;


        for (int i = 0; i < nums.length; i++){
            if (nums[i] > max_number){
                max_number = nums[i];
            }
            if (nums[i] < min_number){
                min_number = nums[i];
            }
        }

        for (int i = 1; i <= min_number; i++){
            if (max_number % i == 0 && min_number % i == 0){
                solution = i;
            }
        }

        return solution;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that returns numbers.");
    }
}
