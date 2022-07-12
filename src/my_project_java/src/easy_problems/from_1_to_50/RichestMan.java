package easy_problems.from_1_to_50;

public class RichestMan implements Numbers{
    public int maximumWealth(int[][] accounts) {

        int solution = -1;
        int count = 0;

        for (int[] account: accounts){
            count = 0;
            for (int money: account){
                count += money;
            }
            solution = Math.max(solution,count);
        }

        return solution;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This solution actually return numbers.");
    }
}
