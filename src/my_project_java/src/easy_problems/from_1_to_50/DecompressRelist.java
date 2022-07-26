package easy_problems.from_1_to_50;

public class DecompressRelist implements Numbers{
    public int[] decompressRLElist(int[] nums) {


        int count = 0;
        int lenNums = nums.length;

        for (int i = 0; i < lenNums; i += 2){
            count += nums[i];
        }

        int[] solution = new int[count];

        count = 0;
        for (int i = 0; i < lenNums; i += 2){
            for ( int j = 0; j < nums[i]; j++){
                solution[count] = nums[i+1];
                count++;
            }
        }

        return solution;


    }


    @Override
    public void returnNumbers() {
        System.out.println("This is a class that does not return numbers.");
    }
}
