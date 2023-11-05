package easy_problems.from_1_to_50;

public class ShuffleArray implements Numbers{
    public int[] shuffle(int[] nums, int n) {

        int lenNums = nums.length;
        int halfLenNums = (int)nums.length/2;
        int[] solution = new int[lenNums];

        for (int i = 0; i<halfLenNums; i++){
            solution[i*2] = nums[i];
            solution[i*2+1] = nums[halfLenNums + i];
        }


        return solution;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This class does not return numbers.");
    }
}
