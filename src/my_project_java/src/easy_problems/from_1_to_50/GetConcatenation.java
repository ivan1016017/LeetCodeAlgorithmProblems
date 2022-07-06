package easy_problems.from_1_to_50;

import java.util.ArrayList;

public class GetConcatenation implements Numbers{
    public GetConcatenation() {
        System.out.println("This is a class that concatenate two list");
    }

    public int[] getConcatenation(int[] nums) {
        
        int numsLength = nums.length;

        int[] solution = new int[numsLength*2];
        
        
        for (int i = 0; i < nums.length; i++){
            solution[i] = solution[i+numsLength] = nums[i];
        }

        return solution;


    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that does not return numbers. It returns concatenated lists instead.");
    }
}
