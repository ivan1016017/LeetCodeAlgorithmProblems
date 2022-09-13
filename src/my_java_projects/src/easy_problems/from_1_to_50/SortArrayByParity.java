package easy_problems.from_1_to_50;

public class SortArrayByParity implements Numbers{


    public int[] sortArrayByParity(int[] nums) {

        int[] solution = new int[nums.length];
        int l = 0;
        int r = nums.length - 1;
        for (int i : nums) {
            if (i % 2 == 0) solution[l++] = i;
            else solution[r--] = i;
        }

        return solution;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of a class that does not return numbers.");
    }
}
