package easy_problems.from_1_to_50;

public class NumberGoodPairs implements Numbers{
    public int numIdenticalPairs(int[] nums) {

        int solution = 0;

        for (int i = 0; i < nums.length; i++){
            for (int j = i+1; j < nums.length; j++){
                if (nums[i] == nums[j]){
                    solution += 1;
                }
            }
        }

        return solution;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that returns the number of good pairs.");
    }
}
