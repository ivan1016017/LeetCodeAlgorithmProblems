package easy_problems.from_1_to_50;

import java.util.Arrays;

public class HeightChecker implements Numbers{
    public int heightChecker(int[] heights) {

        int solution = 0;
        int lenHeights = heights.length;
        int[] original = new int[lenHeights];


        for (int i = 0; i < lenHeights; i++){
            original[i] = heights[i];
        }

        Arrays.sort(heights);

        for (int i = 0; i < lenHeights; i++){
            if (original[i] != heights[i]) solution ++;
        }

        return solution;
    }

    @Override
    public void returnNumbers() {
        System.out.println("This is an instance of the class that does not return numbers");
    }
}
