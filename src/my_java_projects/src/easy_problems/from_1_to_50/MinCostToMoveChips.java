package easy_problems.from_1_to_50;

public class MinCostToMoveChips implements Numbers {
    public int minCostToMoveChips(int[] position) {

        int oddEvent = 0;
        int evenEvent = 0;

        for (int item: position) {
            if (item % 2 == 0) evenEvent++; else oddEvent++;
        }
        return Math.min(oddEvent,evenEvent);
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is a class that return int numbers");
    }
}
