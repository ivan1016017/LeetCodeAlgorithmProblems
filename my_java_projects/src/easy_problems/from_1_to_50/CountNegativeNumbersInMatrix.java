package easy_problems.from_1_to_50;

public class CountNegativeNumbersInMatrix implements Numbers{
    public int countNegatives(int[][] grid) {

        int lenY = grid.length;
        int lenX = grid[0].length;


        int solution = 0;
        for (int i = 0; i < lenY; i++){
            for (int j = 0; j < lenX; j++){
                if (grid[i][j] < 0) {
                    solution = solution + (lenX - j);
                    break;
                }
            }

        }

        return solution;

    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of a class that returns numeric values");
    }
}
