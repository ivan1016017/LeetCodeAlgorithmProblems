package easy_problems.from_1_to_50;

public class FindUniqueIntegersSumUpZero implements Numbers{
    public int[] sumZero(int n) {

        int totalSum = 0;
        int[] solution = new int[n];

        for (int i = 0; i < n-1; i++){
            solution[i] = i+1;
            totalSum -= i+1;
        }

        solution[n-1] = totalSum;

        return solution;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a solution that does not return numeric values.");
    }
}
